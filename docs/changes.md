# Changelog

All notable changes to this project will be documented in this file.

## Unreleased (YYYY-MM-DD)

- Add read the docs.


## 0.2 (2023-10-14)

- Do not issue a user-warning if conda is not installed in the same python-environment.


## 0.1 (2023-10-14)

- Register the monkeypatch as a ``sitecustomize-entrypoints``-plugin.

- Monkey-patch conda's ``conda.core.envs_manager.get_user_environments_txt_file``
  to use an env-var ``CONDA_CACHE_DIR`` and default to ``XDG_CACHE_HOME`` in order
  to avoid writing hardcoded to ``~/.conda/environments.txt``.

- Add boilerplate-files to comply with Github's [_Community Standards_](https://github.com/libranet/autoadd-bindir/community)

- Convert docs from restructured text to markdown.

- Add ``.readthedocs.yaml``.

- Package created by [Wouter Vanden Hove <wouter@libranet.eu>]
