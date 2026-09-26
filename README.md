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

## Installation

The course environment is a pixi environment. Its `pixi.toml` and
`pixi.lock` are in the `pixi` folder of this repo.

### 1. Install pixi

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

Several GB, mostly torch and CUDA.

If you get a chance do at home on good wifi (don't worry if you don't, we'll
give some time to help everyone get setup during the tutorial)

### 3. Check it works

```sh
pixi run jupyter   # JupyterLab
pixi run napari    # napari; the plugins are under Plugins
```

After notebook 12 has downloaded the data, these open napari with AI Lab on
one dataset:

```sh
pixi run bees
pixi run pollen
pixi run ladybugs
```

### Every time you start

From the `pixi` folder of the repo -- it does not work from the repo root:

```sh
cd i2k-2026/pixi
pixi run jupyter
```

Then open `notebooks/10_installation_check.ipynb`.

To run the notebooks in an editor:

- [Using the pixi environment in a VS Code notebook](docs/pixi-in-vscode.md)
- [Using the pixi environment in Jupyter](docs/pixi-in-jupyter.md)

### What is in the environment

napari, the widgets, and the notebook kernel. Also torch and micro_sam:
interactive SAM keeps the image embedding resident between clicks, so it
cannot run out of process.

Every other model stack is built by scikit-ops in its own environment on
first use, under `~/.local/share/appose/`. That first call is slow -- several
GB, then model weights. That is the point of the course.

### Fallback: if pixi gives you trouble

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

Then, every time:

```sh
cd i2k-2026
conda activate i2k2026
jupyter lab
```

Or select that interpreter in VS Code.

An NVIDIA GPU is recommended. Things run on CPU, slowly.

More detail, and the Windows kernel-crash fix, in
[scikit-ops/notebooks/README.md](https://github.com/apposed/scikit-ops/blob/main/notebooks/README.md).

## Contents

Notebooks, in order:

- [`08_getting_started.md`](https://github.com/bnorthan/i2k-2026/blob/main/notebooks/08_getting_started.md) - what the workshop is about, and the install
- `10_installation_check.ipynb` - check the install, run a toy op
- `12_get_the_data.ipynb` - download the bees, ladybugs and pollen images
- `15_build_environments.ipynb` - build the op environments up front, and check the GPU
- `20_cellpose_builtins.ipynb` - Cellpose 3 and 4 built-in models on bees
- `24_receptive_field_circles.ipynb` - StarDist receptive field on circles
- `27_cellpose_train_circles.ipynb` - train Cellpose on circles
- `30_launch_ai_lab.ipynb` - launch ND AI Lab on bees, ladybugs or pollen
- [`32_project_organization.md`](https://github.com/bnorthan/i2k-2026/blob/main/notebooks/32_project_organization.md) - the folders AI Lab keeps in a project
- [`34_annotations.md`](https://github.com/bnorthan/i2k-2026/blob/main/notebooks/34_annotations.md) - from annotations to training patches
- `50_stardist_training_bees.ipynb` - train StarDist on bees
- `52_cellpose_training_bees.ipynb` - train Cellpose on bees
- `53_cellpose_predict_bees.ipynb` - predict bees with a trained Cellpose model

Slides: [`docs/slides.pdf`](docs/slides.pdf)

TODO: schedule
