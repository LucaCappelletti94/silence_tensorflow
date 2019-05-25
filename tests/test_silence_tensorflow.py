import silence_tensorflow
import os

def test_silence_tensorflow():
    """Check that everything runs."""
    assert os.environ["KMP_AFFINITY"] == "noverbose"
    assert os.environ["TF_CPP_MIN_LOG_LEVEL"] == "2"