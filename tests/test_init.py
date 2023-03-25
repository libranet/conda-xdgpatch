# -*- coding: utf-8 -*-
# pylint: disable=import-outside-toplevel
# pylint: disable=missing-function-docstring
"""Testing of module conda_xdgpatch.__init__."""
import packaging.version


def test_version():
    from conda_xdgpatch import __version__

    assert isinstance(__version__, str)
    assert packaging.version.parse(__version__) >= packaging.version.parse("0.0")


def test_copyright():
    from conda_xdgpatch import __copyright__

    assert isinstance(__copyright__, str)
    assert "Libranet" in __copyright__
