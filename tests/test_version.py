"""Tests for the silence_tensorflow package version."""

from validate_version_code import validate_version_code
from silence_tensorflow.__version__ import __version__


def test_version():
    """Check that the version is correctly set."""
    assert validate_version_code(__version__)
