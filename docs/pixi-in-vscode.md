# Using the pixi environment in a VS Code notebook

Assumes pixi is installed and you have cloned this repo. See the
[README](../README.md) for that.

## 1. Build the environment

```sh
cd pixi/i2k2026_lite    # or i2k2026_microsam
pixi install
```

## 2. Register it as a Jupyter kernel

```sh
pixi run register-kernel
```

This adds a kernel named after the folder, whose argv runs through `pixi run` so
the environment activates itself. It is registered for your user, so it shows
up in every notebook on the machine, not just this repo.

This step is not optional on Windows. See below.

## 3. Pick the kernel

Open a notebook. Click **Select Kernel** at the top right.

- Choose **Jupyter Kernel...**
- Choose **i2k2026_lite** or **i2k2026_microsam**

## 4. Check you got the right one

Run this in a cell:

```python
import sys
print(sys.executable)
```

The path must be inside `pixi/i2k2026_lite/.pixi` or `pixi/i2k2026_microsam/.pixi`. If it is not, you are on
a different interpreter and nothing in the course will import.

## Do not select the interpreter directly

**Select Kernel** → **Python Environments...** points VS Code at `python.exe`
with no activation. On Windows that kernel dies on `import napari_ai_lab`:
the environment's `Library\bin` never reaches PATH, so scipy cannot load its
BLAS, and the process aborts with `0xc06d007f` before any traceback.

Always pick the registered **i2k2026_...** kernel under **Jupyter Kernel...**.
Its argv runs through `pixi run`, so it activates itself whoever starts it.

If it does not appear, run `pixi run register-kernel` again and reload the
window.

## Do not pip install into it

If VS Code offers to install `ipykernel` or any other package, decline. The
environment is defined by the folder's `pixi.toml` and rebuilt from
its `pixi.lock`. Packages added by hand are lost on the next
`pixi install`, and they can break the lockfile's versions.

To add a package, put it in `pixi.toml` and run `pixi install` again.

## Removing the kernel

```sh
jupyter kernelspec uninstall i2k2026_lite i2k2026_microsam
```
