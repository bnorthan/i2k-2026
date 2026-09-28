"""Run every course notebook, fast, and report which fail.

    # from pixi/i2k2026_lite or pixi/i2k2026_microsam
    pixi run test-notebooks            # all but 12
    pixi run test-notebooks 20 52      # just these

Runs copies in a temp folder, never the notebooks themselves:

- Training cut to 1 epoch (epochs=N, num_epochs=N).
- 53 predicts with the newest bees_cellpose3_* model in
  data/bees/models/models, since its MODEL is left for students to set.
- 12 is skipped: it downloads the data, which the others need already there.

Leftover scikit-ops workers are killed after each notebook, so one notebook's
GPU memory does not fail the next. That includes workers of any other kernel
you have open.
"""

import json
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
NOTEBOOKS = HERE.parent / "notebooks"
SKIP = {"12"}


def newest_model(prefix):
    models = NOTEBOOKS / "data" / "bees" / "models" / "models"
    found = [
        p for p in models.glob(f"{prefix}*") if not p.name.endswith(".csv")
    ]
    return max(found, key=lambda p: p.stat().st_mtime).name if found else None


def prepare(src, dst):
    nb = json.loads(src.read_text())
    for cell in nb["cells"]:
        if cell["cell_type"] != "code":
            continue
        s = "".join(cell["source"])
        s = re.sub(r"\b(num_)?epochs(\s*=\s*)\d+", r"\1epochs\g<2>1", s)
        if src.name.startswith("53_"):
            model = newest_model("bees_cellpose3_")
            s = re.sub(r'^MODEL = ".*"$', f'MODEL = "{model}"', s, flags=re.M)
        cell["source"] = s.splitlines(True)
        cell["outputs"] = []
        cell["execution_count"] = None
    dst.write_text(json.dumps(nb, indent=1))


def last_error(log):
    lines = [
        l for l in log.splitlines() if re.search(r"Error|Exception", l)
    ]
    return re.sub(r"\x1b\[[0-9;]*m", "", lines[-1]).strip() if lines else ""


def main(only):
    pick = [
        p
        for p in sorted(NOTEBOOKS.glob("[0-9][0-9]_*.ipynb"))
        if p.name[:2] not in SKIP and (not only or p.name[:2] in only)
    ]
    work = Path(tempfile.mkdtemp(prefix="i2k_nbtest_"))
    for p in NOTEBOOKS.iterdir():
        if p.name == "data" or p.name == "images" or p.suffix == ".py":
            (work / p.name).symlink_to(p)
    print(f"Running {len(pick)} notebooks in {work}\n")

    failed = []
    for src in pick:
        nb = work / src.name
        prepare(src, nb)
        start = time.time()
        r = subprocess.run(
            [
                sys.executable, "-m", "jupyter", "nbconvert",
                "--to", "notebook", "--execute", "--output", f"out_{nb.name}",
                "--ExecutePreprocessor.timeout=2000",
                "--ExecutePreprocessor.kernel_name=python3",
                str(nb),
            ],
            cwd=work, capture_output=True, text=True,
            env={**__import__("os").environ, "QT_QPA_PLATFORM": "offscreen"},
        )
        subprocess.run(["pkill", "-f", "share/appose/skop-"])
        took = time.time() - start
        if r.returncode == 0:
            print(f"OK    {src.name}  {took:.0f}s")
        else:
            failed.append(src.name)
            print(f"FAIL  {src.name}  {took:.0f}s  {last_error(r.stderr)}")

    print(f"\n{len(pick) - len(failed)}/{len(pick)} passed. Outputs in {work}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(set(sys.argv[1:])))
