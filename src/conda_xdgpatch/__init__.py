"""conda_xdgpatch.__init__.

- https://github.com/conda/conda/issues/8804
- https://github.com/conda/conda/blob/main/conda/core/envs_manager.py

"""
__version__ = "0.3dev"
__copyright__ = "Copyright 2023 Libranet - All rights reserved."

import os
from os.path import join

try:
    import conda.core.envs_manager
    from conda.common.path import expand

    pre_patched_value = conda.core.envs_manager.get_user_environments_txt_file

except ModuleNotFoundError:
    # conda is not installed in this python-evironment.
    pre_patched_value = None



def get_user_environments_txt_file(userhome: str = "~") -> str:
    """

    Use env-var CONDA_CACHE_DIR if set,
    Otherwise use ~/.cache/conda/environments.txt instead of
    ~/.conda/environments.txt

    /opt/conda/etc/environments.txt
    """
    if cache_dir := os.getenv("CONDA_CACHE_DIR"):
        return expand(join(cache_dir, "environments.txt"))

    cache_dir = os.getenv("XDG_CACHE_HOME", join(userhome, ".cache",))
    return expand(join(cache_dir, "conda", "environments.txt"))


def patch() -> None:
    """Monkeypatch the original function."""
    if not pre_patched_value:
        return

    conda.core.envs_manager.get_user_environments_txt_file = get_user_environments_txt_file



def unpatch() -> None:
    """Unpatch the original function."""
    if not pre_patched_value:
        return

    conda.core.envs_manager.get_user_environments_txt_file = pre_patched_value
