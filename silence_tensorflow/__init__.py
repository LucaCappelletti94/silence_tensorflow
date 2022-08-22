"""Module providing tools to shut up tensorflow useless warnings, letting you focus on the actual problems."""
from .silence_tensorflow import silence_tensorflow
from support_developer import support_luca

support_luca("silence_tensorflow")

__all__ = [
    "silence_tensorflow"
]