"""Module providing tools to shut up tensorflow warnings."""

import os
import logging
from typing import Union, Optional
from enum import Enum
from environments_utils import has_nvidia_gpu, has_amd_gpu


class Level(Enum):
    """Logging level."""

    NONE = "NONE"
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"

    @classmethod
    def from_str(cls, level: str):
        """Get level from string."""
        try:
            return getattr(cls, level.upper())
        except AttributeError as exc:
            raise ValueError(
                f"Invalid logging level: {level}, must be one of {', '.join(cls.__members__)}"
            ) from exc

    def into_logging(self):
        """Get logging level."""
        if self == Level.NONE:
            return logging.CRITICAL
        return getattr(logging, self.value)

    @property
    def min_log_level(self) -> int:
        """Get minimum log level."""
        return {
            Level.NONE: 3,
            Level.ERROR: 2,
            Level.WARNING: 1,
            Level.INFO: 0,
        }[self]

    def __str__(self):
        return self.value


def silence_tensorflow(
    level: Union[str, Level] = Level.NONE,
    disable_onednn: Optional[bool] = None,
):
    """Silence every unnecessary warning from tensorflow.

    Parameters
    ----------
    level : Union[str, Level], optional
        Logging level, by default Level.ERROR
        Can be one of:
        - "NONE": no messages
        - "ERROR": only error messages
        - "WARNING": error messages and warnings
        - "INFO": error messages, warnings and info
    disable_onednn : Optional[bool], optional
        Whether to disable oneDNN, which silences warnings such as:
        "oneDNN custom operations are on. You may see slightly different
         numerical results due to floating-point round-off errors from
         different computation orders. To turn them off, set the environment
         variable `TF_ENABLE_ONEDNN_OPTS=0`.
        By default, it detects whether NVIDIA or AMD GPUs are present and
        disables oneDNN if they are, by default None
    """
    if isinstance(level, str):
        level = Level.from_str(level)

    if not isinstance(level, Level):
        raise ValueError(
            f"Invalid logging level: {level}, must be one of {', '.join(Level.__members__)}"
        )

    logging.getLogger("tensorflow").setLevel(level.into_logging())
    os.environ["KMP_AFFINITY"] = "noverbose"
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = str(level.min_log_level)
    os.environ["GRPC_VERBOSITY"] = str(level)
    os.environ["GLOG_minloglevel"] = str(level.min_log_level)

    # If NVIDIA or AMD GPUs are present, disable oneDNN
    if disable_onednn is None:
        disable_onednn = has_nvidia_gpu() or has_amd_gpu()

    if disable_onednn:
        os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

    try:
        from absl import (  # pylint: disable=import-outside-toplevel
            logging as absl_logging,  # pylint: disable=import-outside-toplevel
        )

        absl_logging.set_verbosity(level.into_logging())

    except (ModuleNotFoundError, ImportError):
        pass

    # We wrap this inside a try-except block
    # because we do not want to be the one package
    # that crashes when TensorFlow is not installed
    # when we are the only package that requires it
    # in a given Jupyter Notebook, such as when the
    # package import is simply copy-pasted.
    try:
        import tensorflow as tf  # pylint: disable=import-outside-toplevel

        tf.get_logger().setLevel(level.into_logging())
        tf.autograph.set_verbosity(level.min_log_level)
    except (ModuleNotFoundError, AttributeError):
        pass
