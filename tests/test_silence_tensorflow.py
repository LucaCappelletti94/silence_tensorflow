"""Tests for silence_tensorflow module."""

import warnings
from silence_tensorflow import silence_tensorflow


def test_silence_tensorflow():
    """Check that everything runs."""
    silence_tensorflow()
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        try:
            import tensorflow as tf  # pylint: disable=import-outside-toplevel, unused-import
        except ModuleNotFoundError:
            pass


def test_silence_tensorflow_level():
    """Check that everything runs."""
    silence_tensorflow("ERROR")
    silence_tensorflow("WARNING")
    silence_tensorflow("INFO")
    silence_tensorflow("NONE")
    silence_tensorflow("DEBUG")


def test_auto_silence():
    """Check that import using auto submodule works."""
    import silence_tensorflow.auto  # pylint: disable=unused-variable, unused-import, import-outside-toplevel, redefined-outer-name
