# 08 — Getting started

**Under construction:** scikit-ops and napari-ai-lab are very new. Expect a
few hiccups, and some changes ahead.

<img src="../docs/images/under_construction.png" alt="Under construction" width="250">

## Scikit-ops

- Ops and runners are new.
- Used to run hard-to-install deep learning.
- Each model gets isolated environment.
- Avoids conflicts with napari.
- Appose handles those installs under the hood.
- Scikit-ops can install environments lazily 
- Host install can stay simpler.


## Install

Here we install the host. Afterwards run notebook 10 to verify your installation.

### Pixi (recommended)

Follow installation instructions for pixi that can be found here [pixi installation page](https://pixi.prefix.dev/latest/installation/).

Reopen the terminal afterwards, so `pixi` is on the path.

Then clone the repo:

```sh
git clone https://github.com/bnorthan/i2k-2026.git
```

If you want a quicker install:

```sh
cd i2k-2026/pixi/i2k2026_lite
pixi install
pixi run register-kernel
```

If you want the cool interactive microsam labeling:

```sh
cd i2k-2026/pixi/i2k2026_microsam
pixi install
pixi run register-kernel
```

- microsam is several GB.
- Mostly torch and CUDA.
- Install at home if you can.
- We'll help during the tutorial.

Then:

- **JupyterLab:** `pixi run jupyter`, from the folder you installed.
- **VS Code:** open the repo, open a notebook, **Select Kernel** →
  **Jupyter Kernel...** → **i2k2026_lite** or **i2k2026_microsam**. Details:
  [pixi in VS Code](../docs/pixi-in-vscode.md).

### pip and conda (fallback)

If pixi fails for you use this. 

```sh
conda create -n i2k2026 -c conda-forge python=3.12 micro_sam
conda activate i2k2026
pip install "scikit-ops @ git+https://github.com/apposed/scikit-ops.git"
pip install napari-ai-lab "tnia-python[plotting]" albumentations jupyterlab matplotlib scikit-image tifffile
```

## Every time you start

**Pixi.**

- **JupyterLab:** `cd i2k-2026/pixi/i2k2026_lite` (or `i2k2026_microsam`), then `pixi run jupyter`
- **VS Code:** open the notebook, pick the **i2k2026_lite** or **i2k2026_microsam** kernel

**Fallback.**

```sh
cd i2k-2026
conda activate i2k2026
jupyter lab
```

Then open `notebooks/10_installation_check.ipynb`.
