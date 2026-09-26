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

Install pixi. Windows, in PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -c "irm -useb https://pixi.sh/install.ps1 | iex"
```

macOS and Linux:

```sh
curl -fsSL https://pixi.sh/install.sh | sh
```

Other options are on the [pixi installation page](https://pixi.prefix.dev/latest/installation/).
Reopen the terminal afterwards, so `pixi` is on the path.

Then build the course environment and start JupyterLab:

```sh
git clone https://github.com/bnorthan/i2k-2026.git
cd i2k-2026/pixi
pixi install
pixi run jupyter
```

`pixi install` is several GB, mostly torch and CUDA.

If you get a chance do at home on good wifi (don't worry if you don't, we'll give some time to help everyone get setup during the tutorial)

### pip and conda (fallback)

Use this only if pixi gives you trouble. micro_sam is only on conda-forge, so
it goes in with conda, and everything else with pip.

```sh
conda create -n i2k2026 -c conda-forge python=3.12 micro_sam
conda activate i2k2026
pip install "scikit-ops @ git+https://github.com/apposed/scikit-ops.git"
pip install "skop-napari @ git+https://github.com/apposed/skop-napari.git"
pip install napari-ai-lab "tnia-python[plotting]" albumentations jupyterlab matplotlib scikit-image tifffile
```

`albumentations` is needed by `napari-ai-lab`'s `AlbumentationsAugmenter`
(used in notebook 52) but is not declared as one of its dependencies, so it
has to be installed explicitly.

## Every time you start

**Pixi.** From the `pixi` folder of the repo -- it does not work from the repo root:

```sh
cd i2k-2026/pixi
pixi run jupyter
```

**Fallback.**

```sh
cd i2k-2026
conda activate i2k2026
jupyter lab
```

Then open `notebooks/10_installation_check.ipynb`.
