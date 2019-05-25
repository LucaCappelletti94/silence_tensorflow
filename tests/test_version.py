from silence_tensorflow.__version__ import __version__
import re

def test_version():
    assert re.compile("\d+\.\d+\.\d+").match(__version__)
