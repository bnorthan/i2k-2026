# 08 — Getting started

**Under construction:** scikit-ops and napari-ai-lab are very new. Expect a
few hiccups, and some changes ahead.

<img src="../docs/images/under_construction.png" alt="Under construction" width="250">

Ops and runners are new. The goal of this workshop is not to understand everything
about them. The main goal of this workshop is learn from a practical perspective how scikit-ops can allow us to run deep learning workflows that are hard to install and combine. 

The motivation behind scikit-ops is to allow very repeatable, very precise,
isolated environments to hold dependencies that potentially conflict with the
host environment — for example, a dependency that can't be installed alongside
the latest version of napari. The scikit-ops framework, via appose, takes care
of the details of that installation. The host dependencies are simple and easy for
the user to install.

Here we install the host. Afterwards run notebook 10 to verify your installation.

## Install

### Pixi (recommended)

Follow installation instructions for pixi that can be found here [pixi installation page](https://pixi.prefix.dev/latest/installation/).

Reopen the terminal afterwards, so `pixi` is on the path.

Then build the course environment and register its kernel:

```sh
git clone https://github.com/bnorthan/i2k-2026.git
cd i2k-2026/pixi
pixi install
pixi run register-kernel
```
`pixi install` is several GB, mostly torch and CUDA.

If you get a chance, do it at home on good wifi (don't worry if you don't, we'll give some time to help everyone get setup during the tutorial)

**Slow download, or no NVIDIA GPU (Linux/Windows)?** Use lite. It skips
micro_sam, torch and CUDA; everything else works, only interactive SAM does not.

```sh
pixi install -e lite
pixi run -e lite register-kernel
```

Then add `-e lite` to `pixi run` commands, and pick the **I2K 2026 (lite)** kernel.

Then :

- **JupyterLab:** `pixi run jupyter`
- **VS Code:** open the repo, open a notebook, **Select Kernel** →
  **Jupyter Kernel...** → **I2K 2026**. Details:
  [pixi in VS Code](../docs/pixi-in-vscode.md).

### pip and conda (fallback)

Use this only if pixi gives you trouble. micro_sam is only on conda-forge, so
it goes in with conda, and everything else with pip.

```sh
conda create -n i2k2026 -c conda-forge python=3.12 micro_sam
conda activate i2k2026
pip install "scikit-ops @ git+https://github.com/apposed/scikit-ops.git"
pip install napari-ai-lab "tnia-python[plotting]" albumentations jupyterlab matplotlib scikit-image tifffile
```

`albumentations` is needed by `napari-ai-lab`'s `AlbumentationsAugmenter`
(used in notebook 52) but is not declared as one of its dependencies, so it
has to be installed explicitly.

## Every time you start

**Pixi.**

- **JupyterLab:** `cd i2k-2026/pixi`, then `pixi run jupyter` (not from the repo root)
- **VS Code:** open the notebook, pick the **I2K 2026** kernel

**Fallback.**

```sh
cd i2k-2026
conda activate i2k2026
jupyter lab
```

Then open `notebooks/10_installation_check.ipynb`.
