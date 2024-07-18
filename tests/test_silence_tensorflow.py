"""Tests for silence_tensorflow module."""

from silence_tensorflow import silence_tensorflow


def test_silence_tensorflow():
    """Check that everything runs."""
    silence_tensorflow()


def test_auto_silence():
    """Check that import using auto submodule works."""
    import silence_tensorflow.auto  # pylint: disable=unused-variable, unused-import, import-outside-toplevel, redefined-outer-name
