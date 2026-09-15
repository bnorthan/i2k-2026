"""Compare a StarDist install across machines.

Runs the same measurements on Linux and Windows and prints one report. The
point is to find why the same notebook is several times slower on one box.

    python diag_stardist.py                 # everything except training
    python diag_stardist.py --epochs 3      # add a short training run

Nothing here takes more than a few seconds unless --epochs is given.
Write the output to a file and commit it, so the two machines can be diffed:

    python diag_stardist.py --epochs 3 > diag_<hostname>.txt
"""

import argparse
import os
import platform
import socket
import sys
import time

import numpy as np


def section(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


def phantom(size=256, n=12, seed=0):
    """A small label image: same on every machine, so timings compare."""
    rng = np.random.default_rng(seed)
    lbl = np.zeros((size, size), np.uint16)
    yy, xx = np.mgrid[:size, :size]
    for i in range(n):
        cy = rng.integers(30, size - 30)
        cx = rng.integers(30, size - 30)
        r = rng.integers(5, 40)
        lbl[(yy - cy) ** 2 + (xx - cx) ** 2 < r * r] = i + 1
    return lbl


def report_machine():
    section("machine")
    print("host      ", socket.gethostname())
    print("platform  ", platform.platform())
    print("python    ", sys.version.split()[0], "@", sys.executable)
    print("cores     ", os.cpu_count())
    print("processor ", platform.processor() or "(unknown)")
    for var in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "KMP_DUPLICATE_LIB_OK",
                "CUDA_VISIBLE_DEVICES", "OMP_THREAD_LIMIT"):
        print("  %-22s %s" % (var, os.environ.get(var)))


def report_versions():
    section("versions")
    for name in ("numpy", "scipy", "stardist", "csbdeep", "tensorflow",
                 "gputools", "pyopencl", "numba"):
        try:
            mod = __import__(name)
            print("  %-12s %s" % (name, getattr(mod, "__version__", "?")))
        except ImportError:
            print("  %-12s MISSING" % name)


def report_extension():
    """Whether the compiled star_dist links an OpenMP runtime.

    stardist's 0.9.x Windows wheels ship without one, which makes target
    generation single-threaded and training many times slower.
    """
    section("compiled extension")
    try:
        import stardist.lib.stardist2d as ext
    except Exception as exc:  # pragma: no cover - diagnostic only
        print("  cannot import stardist.lib.stardist2d:", exc)
        return

    path = getattr(ext, "__file__", None)
    print("  ", path)
    if not path or not os.path.isfile(path):
        return

    with open(path, "rb") as handle:
        blob = handle.read().lower()
    for marker, label in ((b"vcomp", "VCOMP (MSVC OpenMP)"),
                          (b"libgomp", "libgomp (GCC OpenMP)"),
                          (b"libomp", "libomp (LLVM OpenMP)")):
        if marker in blob:
            print("   openmp runtime referenced:", label)
            break
    else:
        print("   NO OpenMP runtime referenced -> star_dist is single-threaded")


def time_call(fn, repeat=5):
    fn()
    wall, cpu = time.time(), time.process_time()
    for _ in range(repeat):
        fn()
    return (time.time() - wall) / repeat, (time.process_time() - cpu)


def report_star_dist():
    """The function that dominates a StarDist epoch at grid=(1,1)."""
    section("star_dist (target generation)")
    from stardist import star_dist

    lbl = phantom()
    wall, cpu = time_call(lambda: star_dist(lbl, 32, mode="cpp"))
    print("  cpp     %7.1f ms/call   cpu/wall %5.2f   (cores %d)"
          % (wall * 1000, cpu / (wall * 5), os.cpu_count()))
    print("          cpu/wall near 1.0 means one core; near the core count")
    print("          means OpenMP is working.")

    try:
        wall, _ = time_call(lambda: star_dist(lbl, 32, mode="opencl"))
        print("  opencl  %7.1f ms/call" % (wall * 1000))
    except Exception as exc:
        print("  opencl  unavailable: %s" % type(exc).__name__)


def report_generator():
    """Per-sample cost of the training data pipeline, without TensorFlow."""
    section("StarDistData2D (training data pipeline)")
    try:
        import circles
    except ImportError:
        print("  circles.py not importable from", os.getcwd())
        return
    from stardist.models.model2d import StarDistData2D

    imgs, lbls = circles.random(8, size=256, min_r=1, max_r=85, seed=1)
    frac = float(np.mean([(l > 0).mean() for l in lbls]))
    print("  8 images, %.1f%% foreground, objects to r=85" % (frac * 100))

    X = [np.asarray(i, np.float32)[..., np.newaxis] for i in imgs]
    Y = [np.asarray(l, np.uint16) for l in lbls]

    for grid in (1, 2):
        gen = StarDistData2D(X, Y, batch_size=1, n_rays=32, length=1000,
                             patch_size=(256, 256), grid=(grid, grid))
        it = iter(gen)
        next(it)
        t0 = time.time()
        for _ in range(20):
            next(it)
        per = (time.time() - t0) / 20
        print("  grid=(%d,%d)  %6.1f ms/sample  -> %5.1f s per 50-step epoch"
              % (grid, grid, per * 1000, per * 50))


def report_tensorflow():
    section("tensorflow / gpu")
    import tensorflow as tf

    for gpu in tf.config.list_physical_devices("GPU"):
        try:
            tf.config.experimental.set_memory_growth(gpu, True)
        except RuntimeError:
            pass

    print("  version        ", tf.__version__)
    print("  built with cuda", tf.test.is_built_with_cuda())
    gpus = tf.config.list_physical_devices("GPU")
    print("  gpus           ", gpus or "NONE")
    for gpu in gpus:
        try:
            print("   ", tf.config.experimental.get_device_details(gpu))
        except Exception:
            pass

    x = tf.random.normal([8, 256, 256, 32])
    conv = tf.keras.layers.Conv2D(32, 3, padding="same")

    def bench(device):
        with tf.device(device):
            conv(x).numpy()
            t0 = time.time()
            for _ in range(20):
                y = conv(x)
            y.numpy()
            return (time.time() - t0) / 20 * 1000

    if gpus:
        print("  conv GPU  %6.2f ms/iter" % bench("/GPU:0"))
    print("  conv CPU  %6.2f ms/iter" % bench("/CPU:0"))


def report_training(epochs):
    section("training (%d epochs, 50 steps, patch 256, batch 1, grid 1)" % epochs)
    import tensorflow as tf
    import circles
    from stardist.models import Config2D, StarDist2D

    imgs, lbls = circles.random(8, size=256, min_r=1, max_r=85, seed=1)
    X = [np.asarray(i, np.float32)[..., np.newaxis] for i in imgs]
    Y = [np.asarray(l, np.int32) for l in lbls]

    times = []

    class Timer(tf.keras.callbacks.Callback):
        def on_epoch_begin(self, epoch, logs=None):
            self._t0 = time.time()

        def on_epoch_end(self, epoch, logs=None):
            times.append(time.time() - self._t0)
            print("  epoch %d: %.2f s" % (epoch + 1, times[-1]), flush=True)

    config = Config2D(n_rays=32, axes="YXC", n_channel_in=1,
                      train_patch_size=(256, 256), train_batch_size=1,
                      unet_n_depth=4, grid=(1, 1))
    net = StarDist2D(config=config, name="diag_net",
                     basedir=os.path.join(os.path.expanduser("~"), "i2k_diag"))
    net.prepare_for_training()
    net.callbacks.append(Timer())
    fit = net.keras_model.fit
    net.keras_model.fit = lambda *a, **kw: fit(*a, **{**kw, "verbose": 0})

    net.train(X + X, Y + Y, validation_data=(X, Y),
              epochs=epochs, steps_per_epoch=50)

    steady = times[1:] or times
    print("  median %.2f s/epoch" % float(np.median(steady)))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--epochs", type=int, default=0,
                        help="also run this many training epochs (0 = skip)")
    args = parser.parse_args()

    report_machine()
    report_versions()
    report_extension()
    report_star_dist()
    report_generator()
    report_tensorflow()
    if args.epochs:
        report_training(args.epochs)
    print()
    print("done")


if __name__ == "__main__":
    main()
