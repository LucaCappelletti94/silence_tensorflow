# Silence TensorFlow

[![pip](https://badge.fury.io/py/silence-tensorflow.svg)](https://pypi.org/project/silence-tensorflow/)
[![python](https://img.shields.io/pypi/pyversions/silence-tensorflow)](https://pypi.org/project/silence-tensorflow/)
[![license](https://img.shields.io/pypi/l/silence-tensorflow)](https://pypi.org/project/silence-tensorflow/)
[![downloads](https://pepy.tech/badge/silence-tensorflow)](https://pepy.tech/project/silence-tensorflow)
[![Github Actions](https://github.com/LucaCappelletti94/silence_tensorflow/actions/workflows/python.yml/badge.svg)](https://github.com/LucaCappelletti94/silence_tensorflow/actions/)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/e6fe64db1c9042bbaa4c0a20bde585dc)](https://app.codacy.com/gh/LucaCappelletti94/silence_tensorflow/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

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

### Setting the logging level

While by default the logging level is set to error, you can set it to any level you want by passing the level as an argument to the function.

```python
from silence_tensorflow import silence_tensorflow

# Set the logging level to error, meaning only errors will be logged
silence_tensorflow("ERROR")

# Set the logging level to warning, meaning only errors and warnings will be logged
silence_tensorflow("WARNING")

# Set the logging level to info, meaning errors, warnings and info will be logged
silence_tensorflow("INFO")

# Set the logging level to debug, meaning all logs will be shown
silence_tensorflow("DEBUG")
```

## Can it be done within the import?

Sure, you can do everything with a single line by importing the submodule auto.

This will set the logging level to error and the affinity to no verbose.

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

## Known limitations

While I really tried to cover all possible logs that TensorFlow can produce, there are some logs that are not silenced by this package.
Below you find the ones that we are aware of, alongside the reason why they are not silenced and what you can do to silence them.

### NUMA node read from SysFS had negative value

You may have encountered the following log:

```plaintext
successful NUMA node read from SysFS had negative value (-1)
```

This log means that TensorFlow is trying to read the NUMA node from the system file system and it is getting a negative value. This is not an error, but a warning, and this package cannot silence it automatically without administrative privileges. Since executing code you have just found online with administrative privileges is not a good idea, you can silence this log by running as root the following command in your terminal:

```bash
for a in /sys/bus/pci/devices/*; do echo 0 | sudo tee -a $a/numa_node; done
```

This command will set the NUMA node to 0 for all PCI devices, which is the default value and should not cause any issues. It does not fix the underlying issue, but it silences the log until you reboot your system.

### TensorFlow Lite (TFLite)

TFLite logs are not silenced by this package because [they have hardcoded the logging level to `INFO`](https://github.com/tensorflow/tensorflow/blob/3570f6d986066b834a7f54f3c3ec60d0245193bd/tensorflow/lite/minimal_logging_ios.cc#L50) and there is no way to change it from the Python side.

TFLite will cause info logs such as the following to be printed:

```plaintext
INFO: Created TensorFlow Lite XNNPACK delegate for CPU.
```

If you are willing to recompile your own version of TensorFlow Lite, you can change the logging level to `ERROR` by changing the line mentioned above or set it in your C++ code as follows, [as described in this issue](https://github.com/tensorflow/tensorflow/issues/58050#issuecomment-1624919480):

```cpp
tflite::LoggerOptions::SetMinimumLogSeverity(tflite::TFLITE_LOG_SILENT);
```

### oneDNN warning

Another common warning that TensorFlow prints is the following:

```plaintext
I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
```

I tried to automatically set the environment variable `TF_ENABLE_ONEDNN_OPTS` to `0` when GPU drivers are detected and in such cases using oneDNN is not necessary. However, this in some instances lead to TensorFlow __occasionally__ deadlocking and I had to revert the change.

## License

This software is distributed under the MIT License.
