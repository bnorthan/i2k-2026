# 67 — Your own data

Open AI Lab on your own images, with no script.

## Put your images in a folder

- One folder, just the images.

## Start napari

Any of these, in the course environment:

- From `pixi/i2k2026_lite` or `pixi/i2k2026_microsam`: `pixi run napari`
- From a notebook: `import napari; napari.Viewer()`

## Open AI Lab

- **Plugins → Napari AI Lab → 2D Instance AI Lab**
- **Open Project**
  - **Browse...** to your folder
  - **Viewer type:** sequence
  - RGB images: **Axes to collapse** `C`, **Axis types** `NYXC`
- **OK**
