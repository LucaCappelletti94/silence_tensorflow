from silence_tensorflow import silence_tensorflow

def test_silence_tensorflow():
    """Check that everything runs."""
    silence_tensorflow()

def test_auto_silence():
    import silence_tensorflow.auto # noqa # pylint: disable=unused-import