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

- **[scikit-ops](https://github.com/apposed/scikit-ops)** — an op collection,
  and an implementation of an op runner.
- **[napari-ai-lab](https://github.com/True-North-Intelligent-Algorithms/napari-ai-lab)**
  — interactive segmentation, labelling, correction and training, with each
  model running in its own environment.

## Installation

Everything is in
[`notebooks/08_getting_started.md`](notebooks/08_getting_started.md): pixi,
the lite option, VS Code, and a pip/conda fallback.

In short:

Install pixi. Windows, in PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -c "irm -useb https://pixi.sh/install.ps1 | iex"
```

macOS and Linux:

```sh
curl -fsSL https://pixi.sh/install.sh | sh
```

Other options are on the
[pixi installation page](https://pixi.prefix.dev/latest/installation/).
Reopen the terminal afterwards, so `pixi` is on the path. Then:

```sh
git clone https://github.com/bnorthan/i2k-2026.git
cd i2k-2026/pixi
pixi install
pixi run register-kernel
pixi run jupyter
```

Then run notebooks 10, 12 and 15.

An NVIDIA GPU is recommended. Things run on CPU, slowly.

## Contents

Notebooks, in order:

- [`08_getting_started.md`](https://github.com/bnorthan/i2k-2026/blob/main/notebooks/08_getting_started.md) - what the workshop is about, and the install
- `10_installation_check.ipynb` - check the install, run a toy op
- `12_get_the_data.ipynb` - download the bees, ladybugs and pollen images
- `15_build_environments.ipynb` - build the op environments up front, and check the GPU
- `20_cellpose_builtins.ipynb` - Cellpose 3 and 4 built-in models on bees
- `22_cellcast.ipynb` - CellCast, StarDist without TensorFlow
- `24_receptive_field_circles.ipynb` - StarDist receptive field on circles
- `27_cellpose_train_circles.ipynb` - train Cellpose on circles
- `30_launch_ai_lab.ipynb` - launch ND AI Lab on bees, ladybugs or pollen
- [`32_project_organization.md`](https://github.com/bnorthan/i2k-2026/blob/main/notebooks/32_project_organization.md) - the folders AI Lab keeps in a project
- [`33_ex_01_find_the_pollen.md`](notebooks/33_ex_01_find_the_pollen.md) - exercise 1: find the pollen with Cellpose
- [`34_annotations.md`](https://github.com/bnorthan/i2k-2026/blob/main/notebooks/34_annotations.md) - from annotations to training patches
- `50_stardist_training_bees.ipynb` - train StarDist on bees
- `52_cellpose_training_bees.ipynb` - train Cellpose on bees
- `53_cellpose_predict_bees.ipynb` - predict bees with a trained Cellpose model
- [`60_ex_02_find_the_bees.md`](notebooks/60_ex_02_find_the_bees.md) - exercise 2: label and train on bees
- [`65_ex_03_find_the_ladybugs.md`](notebooks/65_ex_03_find_the_ladybugs.md) - exercise 3: label and train on ladybugs
- [`67_your_own_data.md`](notebooks/67_your_own_data.md) - open your own images in AI Lab

Slides: [`docs/slides.pdf`](docs/slides.pdf)

