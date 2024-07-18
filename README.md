# Silence TensorFlow

[![pip](https://badge.fury.io/py/silence-tensorflow.svg)](https://pypi.org/project/silence-tensorflow/)
[![python](https://img.shields.io/pypi/pyversions/silence-tensorflow)](https://pypi.org/project/silence-tensorflow/)
[![license](https://img.shields.io/pypi/l/silence-tensorflow)](https://pypi.org/project/silence-tensorflow/)
[![downloads](https://pepy.tech/badge/silence-tensorflow)](https://pepy.tech/project/silence-tensorflow)
[![Github Actions](https://github.com/LucaCappelletti94/silence-tensorflow/actions/workflows/python.yml/badge.svg)](https://github.com/LucaCappelletti94/silence-tensorflow/actions/)

Python package to shut up TensorFlow warnings and logs, letting you focus on the important errors.

## How do I install this package?

As usual, just download it using pip:

```shell
pip install silence_tensorflow
```

## How do I use it?

You only need to import the package before importing TensorFlow:

```python
from silence_tensorflow import silence_tensorflow
silence_tensorflow()
import tensorflow as tf

# your code
```

## Can it be done within the import?

Sure, you can do everything with a single line by importing the submodule auto:

```python
import silence_tensorflow.auto
import tensorflow as tf

# your code
```

## How can I get pylint to ignore the unused import?

You can use the flag `disable=unused-import` as such:

```python
import silence_tensorflow.auto  # pylint: disable=unused-import
import tensorflow as tf

# your code
```

## How can I get pylint to ignore the unused variable?

If you import `silence_tensorflow` in the context of a function you will get a different warning from pylint: unused variable. You can use the flag `disable=unused-variable` as such:

```python
def func():
    import silence_tensorflow.auto  # pylint: disable=unused-variable
    import tensorflow as tf

    # your code
```

## How does this work under the hood?

This package will set the `KMP_AFFINITY` system variable to `noverbose` and `TF_CPP_MIN_LOG_LEVEL` to level `3` (only errors logged).

If you need a custom value for `KMP_AFFINITY` you should reset it after importing the package, as follows:

```python
import os
from silence_tensorflow import silence_tensorflow
backup = os.environ["KMP_AFFINITY"]
silence_tensorflow()
os.environ["KMP_AFFINITY"] = backup
```
