[![Testing](https://img.shields.io/github/actions/workflow/status/libranet/conda-xdgpatch/testing.yaml?branch=main&longCache=true&style=flat-square&label=tests&logo=GitHub%20Actions&logoColor=fff")](https://github.com/libranet/conda-xdgpatch/actions/workflows/testing.yaml)
[![Read the Docs](https://readthedocs.org/projects/conda-xdgpatch/badge/?version=latest)](https://conda-xdgpatch.readthedocs.io/en/latest/)
[![PyPi Package](https://img.shields.io/pypi/v/conda-xdgpatch?color=%2334D058&label=pypi%20package)](https://pypi.org/project/conda-xdgpatch/)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/libranet/conda-xdgpatch/blob/main/docs/license.md)



## Installation

On your base conda-installation, install via pip:

```bash
> cd /opt/tools/conda
> bin/pip install conda-xdgpatch
```



## Usage

Just use conda to create conda-environments.


## Registered sitecustomize-entrypoint

The ``conda_xdgpatch.patch``-function is registered as a ``sitecustomize``-entrypoint in our pyproject.toml_:

``` toml
    [tool.poetry.plugins]
    [tool.poetry.plugins."sitecustomize"]
    conda_xdgpatch = "conda_xdgpatch:patch"
```

Sitecustomize and all its registered entrypoints will be executed at the start of *every* python-process.
For more information, please see [sitecustomize-entrypoints](http://pypi.python.org/pypi/sitecustomize-entrypoints)


## Compatibility

 [![Python Version](https://img.shields.io/pypi/pyversions/conda-xdgpatch?:alt:PyPI-PythonVersion)](https://pypi.org/project/conda-xdgpatch/)
 [![PyPI - Implementation](https://img.shields.io/pypi/implementation/conda-xdgpatch?:alt:PyPI-Implementation)](https://pypi.org/project/conda-xdgpatch/)

``conda-xdgpatch``  works on Python 3.8+, including PyPy3. Tested until Python 3.11,


## Notable dependencies

- [conda](http://pypi.python.org/pypi/conda
- [sitecustomize-entrypoints](http://pypi.python.org/pypi/sitecustomize-entrypoints)