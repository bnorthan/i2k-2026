# Jupyter Notebooks and Napari Plugins for Deep Learning Segmentation and Restoration

**I2K 2026**

A short course on GPU and deep learning segmentation and restoration in Jupyter
and Napari, where complex and incompatible python dependencies are handled by
running each method in its own environment.

## About

The goal of this workshop is to run and compare different approaches —
Cellpose, StarDist, classical image processing, gpu deconvolution — in one
workflow, whether that is a script, a notebook or a napari plugin. This is
normally hard because the libraries need incompatible dependencies. We show
how appose, pixi and scikit-ops address that, and work through use cases
using both notebooks and napari plugins.

## Projects used in this workshop

- **[scikit-ops](https://github.com/apposed/scikit-ops)** — the ops, plus the
  machinery that runs each one in its own environment. We work through
  notebooks on deconvolution, Cellpose and YOLO-SAM:
  [basics](https://github.com/apposed/scikit-ops/blob/main/notebooks/00-basics.ipynb) ·
  [edge handling in deconvolution](https://github.com/apposed/scikit-ops/blob/main/notebooks/deconvolution/bead-edge-handling.ipynb) ·
  [Cellpose from skop](https://github.com/apposed/scikit-ops/blob/main/notebooks/segmentation/cellpose_mixed.ipynb) ·
  [box and mask detectors](https://github.com/apposed/scikit-ops/blob/main/notebooks/detection/detect-then-mask.ipynb)
- **[skop-napari](https://github.com/apposed/skop-napari)** — the same ops in
  napari. A GUI is generated from the op's signature, so a workflow written in
  a notebook runs in the viewer without a plugin being written by hand, and
  workflow ops can be shipped as plugins.
- **[napari-ai-lab](https://github.com/True-North-Intelligent-Algorithms/napari-ai-lab)**
  — interactive segmentation, labelling, correction and training, with each
  model running in its own environment.

Rough order: ops in notebooks, then the same ops as plugins, then the
annotation and training workflow on top.

## Contents

TODO — notebooks, environments, schedule.

## Early bird installation

For anyone who wants to try things before the course. Expect this to change.
scikit-ops and skop-napari are not on PyPI yet, so the lockfile pins them
from git.

The course environment is a pixi environment. Pixi reads a lockfile, so
everyone gets the same versions on Windows, macOS and Linux.

### 1. Install pixi

Windows installer

Follow instructions [here](https://pixi.prefix.dev/latest/installation/#__tabbed_1_2)

Windows, in PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -c "irm -useb https://pixi.sh/install.ps1 | iex"
```

macOS and Linux:

```sh
curl -fsSL https://pixi.sh/install.sh | sh
```

Other options -- MSI, winget, scoop, Homebrew -- are on the
[pixi installation page](https://pixi.prefix.dev/latest/installation/).

Reopen the terminal afterwards, so `pixi` is on the path.

### 2. Build the environment

```sh
git clone https://github.com/bnorthan/i2k-2026.git
cd i2k-2026/pixi
pixi install
```

Several GB, mostly torch and CUDA. Do this at home on good wifi, not in the
room.

### 3. Check it works

```sh
pixi run jupyter   # JupyterLab
pixi run lab # should start napari with the ai-lab plugin and an imageset loaded
pixi run napari    # napari; the plugins are under Plugins
```

To run the notebooks in an editor:

- [Using the pixi environment in a VS Code notebook](docs/pixi-in-vscode.md)
- [Using the pixi environment in Jupyter](docs/pixi-in-jupyter.md)

### What is in the environment

napari, the widgets, and the notebook kernel. Also torch, micro_sam and
cellpose: interactive SAM keeps the image embedding resident between clicks,
so it cannot run out of process.

Every other model stack is built by scikit-ops in its own environment on
first use, under `~/.local/share/appose/`. That first call is slow -- several
GB, then model weights. That is the point of the course.

### Fallback: if pixi gives you trouble

This path skips pixi. It runs the notebooks and the ops, but **not**
interactive segmentation: it installs no micro_sam, so the interactive SAM
parts of the course will not work. Use it to keep going, not as the
course environment.

Python 3.12 or newer (skop-napari needs it), in a venv or conda env:

```sh
pip install "scikit-ops @ git+https://github.com/apposed/scikit-ops.git"
pip install "skop-napari @ git+https://github.com/apposed/skop-napari.git"
pip install napari-ai-lab
pip install "napari[all]" jupyterlab matplotlib scikit-image tifffile
```

Then `jupyter lab`, or select that interpreter in VS Code.

An NVIDIA GPU is recommended. Things run on CPU, slowly.

More detail, and the Windows kernel-crash fix, in
[scikit-ops/notebooks/README.md](https://github.com/apposed/scikit-ops/blob/main/notebooks/README.md).
