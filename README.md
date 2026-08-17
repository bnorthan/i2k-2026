# Jupyter Notebooks and Napari Plugins for Deep Learning Segmentation and Restoration

**I2K 2026**

A short course on GPU and deep learning segmentation and restoration in Jupyter
and Napari, where each method runs in its own environment.

## About

Strategies for setting up Jupyter notebooks and napari plugins for deep
learning restoration and segmentation. The goal is to compare different
approaches — Cellpose, StarDist, classical image processing — in one workflow,
whether that is a script, a notebook or a napari plugin. This is normally hard
because the libraries need incompatible dependencies. We show how appose, pixi
and cellcast address that, and work through three projects built on them.

## The three projects

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

For anyone who wants to try things before the course. Expect this to change —
scikit-ops and skop-napari are not on PyPI yet, so for now they come from git.

**The one thing to understand first:** the environment you install below is a
*host*. It holds the notebook kernel, napari and the widgets — no torch, no
Cellpose, no CUDA. Each op runs in its own environment, built the first time
you call it, into `~/.local/share/appose/`. So the first run that touches a
real model is slow: several GB per stack, then model weights. That is the
point of the course, but it is worth doing at home on good wifi rather than in
the room.

Python 3.12 or newer (skop-napari needs it), in a venv, conda env or pixi
environment:

```sh
pip install "scikit-ops @ git+https://github.com/apposed/scikit-ops.git"
pip install "skop-napari @ git+https://github.com/apposed/skop-napari.git"
pip install napari-ai-lab
pip install "napari[all]" jupyterlab matplotlib scikit-image tifffile
```

Then check it works — this builds an environment and will take a while:

```sh
jupyter lab   # and run notebooks/00-basics.ipynb from a scikit-ops checkout
napari        # the plugins appear under Plugins
```

An NVIDIA GPU is recommended. Things run on CPU, slowly.

More detail, and the Windows kernel-crash fix, in
[scikit-ops/notebooks/README.md](https://github.com/apposed/scikit-ops/blob/main/notebooks/README.md).
