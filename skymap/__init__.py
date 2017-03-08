"""
Skymap
======

Provides utilities for plotting skymaps.
"""
__author__ = 'Alex Drlica-Wagner'
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

from skymap.core import Skymap, McBrydeSkymap, OrthoSkymap
