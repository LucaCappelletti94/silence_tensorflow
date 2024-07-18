"""Test the corner cases of the silence_tensorflow function."""

import pytest
from silence_tensorflow import silence_tensorflow


def test_corner_cases():
    """Test the corner cases of the silence_tensorflow function."""

    with pytest.raises(ValueError):
        silence_tensorflow(1)

    with pytest.raises(ValueError):
        silence_tensorflow("1")
