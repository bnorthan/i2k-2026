"""Start napari with ND AI Lab open on one of the course datasets.

Run through the pixi tasks, from this folder:

    pixi run bees
    pixi run pollen
    pixi run ladybugs

A profile name after the task picks what AI Lab offers, e.g.
`pixi run bees all`. The default is 2d-instance-skop, as in notebook 30.

The data comes from notebooks/12_get_the_data.ipynb, which puts it in
notebooks/data/. Same settings as notebooks/30_launch_ai_lab.ipynb.
"""

import sys
from pathlib import Path

# Task name -> folder under notebooks/data/
DATASETS = {
    "bees": "bees",
    "pollen": "pollen_count",
    "ladybugs": "ladybugs",
}

if len(sys.argv) < 2 or sys.argv[1] not in DATASETS:
    sys.exit(f"usage: launch_lab.py {{{'|'.join(DATASETS)}}} [profile]")

name = sys.argv[1]
profile = sys.argv[2] if len(sys.argv) > 2 else "2d-instance-skop"

data = Path(__file__).resolve().parent.parent / "notebooks" / "data"
project = data / DATASETS[name]
if not project.is_dir():
    sys.exit(
        f"{project} not found. Run notebooks/12_get_the_data.ipynb first "
        "to download the data."
    )

import napari
from napari_ai_lab.apps.nd_ai_lab_launcher import launch_nd_ai_lab

viewer = napari.Viewer()

ai_lab, sequence_viewer, model = launch_nd_ai_lab(
    viewer,
    project,
    viewer_type="sequence",
    axes_to_collapse="C",
    axis_types="NYXC",
    register_all=True,
    profile=profile,
)

print("ND AI Lab launched on", project.name)
napari.run()
