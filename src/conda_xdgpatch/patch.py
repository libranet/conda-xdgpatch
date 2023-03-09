"""conda_xdgpatch.patch

- https://github.com/conda/conda/issues/8804
- https://github.com/conda/conda/blob/main/conda/core/envs_manager.py



libranet_conda
conda-xdgpatch
sitecustomize-conda-xdgpatch


"""
import os
from os.path import join

import conda.core.envs_manager
from conda.common.path import expand

pre_patched_value = conda.core.envs_manager.get_user_environments_txt_file

def get_user_environments_txt_file(userhome:str="~") -> str:
    """
    Use ~/.cache/conda/environments.txt instead of
    ~/.conda/environments.txt

    /opt/conda/etc/environments.txt
    """
    cache_dir = os.getenv("XDG_CACHE_HOME", join(userhome, '.cache'))
    return expand(join(cache_dir, 'conda', 'environments.txt'))


def patch() -> None:
    """Monkeypatch the original function."""
    conda.core.envs_manager.get_user_environments_txt_file = get_user_environments_txt_file


def unpatch() -> None:
    """Unpatch the original function."""
    conda.core.envs_manager.get_user_environments_txt_file = pre_patched_value
