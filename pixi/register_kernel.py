"""Register this pixi environment as a Jupyter kernel that activates itself.

ipykernel's own installer writes argv from sys.executable: the bare
interpreter, with no activation. That works when the Jupyter server was
started with `pixi run`, because the kernel inherits the server's PATH. It
breaks when a client launches the kernelspec directly, as VS Code does. The
environment's Library/bin never reaches PATH, scipy cannot find its
delay-loaded BLAS, and the kernel dies importing skimage with 0xc06d007f.

Routing argv through `pixi run` makes the kernel activate itself, whoever
starts it.
"""

import json
import sys
import tempfile
from pathlib import Path

from jupyter_client.kernelspec import KernelSpecManager

NAME = "i2k2026"
DISPLAY = "I2K 2026"

manifest = Path(__file__).resolve().parent / "pixi.toml"
if not manifest.exists():
    sys.exit(f"no pixi.toml beside {Path(__file__).name}")

spec = {
    "argv": [
        "pixi",
        "run",
        "--manifest-path",
        str(manifest),
        "python",
        "-Xfrozen_modules=off",
        "-m",
        "ipykernel_launcher",
        "-f",
        "{connection_file}",
    ],
    "display_name": DISPLAY,
    "language": "python",
    "metadata": {"debugger": True},
}

with tempfile.TemporaryDirectory() as tmp:
    staged = Path(tmp) / NAME
    staged.mkdir()
    (staged / "kernel.json").write_text(
        json.dumps(spec, indent=1), encoding="utf-8"
    )
    dest = KernelSpecManager().install_kernel_spec(
        str(staged), kernel_name=NAME, user=True
    )

print(f"Registered {DISPLAY!r} as {NAME!r} in {dest}")
print("Its argv goes through `pixi run`, so the kernel activates itself.")
