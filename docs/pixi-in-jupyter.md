# Using the pixi environment in Jupyter

Assumes pixi is installed and you have cloned this repo. See the
[README](../README.md) for that.

## Which Jupyter

**JupyterLab.** That is the current one, and it is in this environment
already.

If you remember IPython Notebook: it was renamed Jupyter Notebook, and
Notebook 7 is now built on JupyterLab. Either front end works. JupyterLab is
what the course uses.

## The short way

```sh
cd pixi
pixi install
pixi run jupyter
```

`pixi run jupyter` starts JupyterLab from inside the environment. The default
kernel is already the right one. Nothing to register, nothing to select.

Use this if you only run these notebooks.

The file browser on the left opens at the repo root. The course notebooks are
in `notebooks/`. Open one and it runs in this environment.

The first tab you see is the Launcher, which offers tiles for starting a blank
notebook. You do not need it. Use the file browser.


## The other way: register a kernel

Use this if you have your own Jupyter and want to launch it yourself.

```sh
cd pixi
pixi run register-kernel
```

That adds a kernel named **I2K 2026**. Then start your own Jupyter and pick
it from the kernel list.

The kernel is registered for your user, so it appears in every notebook on
the machine.

## Check you got the right one

Run this in a cell:

```python
import sys
print(sys.executable)
```

The path must be inside `pixi/.pixi/envs/default`. If it is not, you are on
a different interpreter and nothing in the course will import.

## Do not pip install into it

The environment is defined by `pixi/pixi.toml` and rebuilt from
`pixi/pixi.lock`. Packages added by hand are lost on the next `pixi install`,
and they can break the lockfile's versions.

To add a package, put it in `pixi.toml` and run `pixi install` again.

## Removing the kernel

```sh
jupyter kernelspec uninstall i2k2026
```
