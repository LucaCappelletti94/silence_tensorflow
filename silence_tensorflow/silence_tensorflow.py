"""Module providing tools to shut up tensorflow warnings."""

import os
import logging
from typing import Union
from enum import Enum


class Level(Enum):
    """Logging level."""

    NONE = "NONE"
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"

    @classmethod
    def from_str(cls, level: str) -> "Level":
        """Get level from string."""
        if level == "DEBUG":
            level = "INFO"
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

    def __str__(self) -> str:
        return self.value


def silence_tensorflow(
    level: Union[str, Level] = Level.NONE,
) -> None:
    """Silence every unnecessary warning from tensorflow.

    Parameters
    ----------
    level : Union[str, Level], optional
        Logging level, by default Level.ERROR
        Can be one of:
        - "NONE": no messages
        - "ERROR": only error messages
        - "WARNING": error messages and warnings
        - "INFO" or "DEBUG": error messages, warnings and info
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
