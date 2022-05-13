Silence TensorFlow
=========================================================================================
|pip| |downloads|

Simple python package to shut up Tensorflow warnings and logs, letting you focus on the 
important errors.

How do I install this package?
----------------------------------------------
As usual, just download it using pip:

.. code:: shell

    pip install silence_tensorflow


How do I use it?
----------------------------------------
You only need to import the package before import Tensorflow:

.. code:: python

    from silence_tensorflow import silence_tensorflow
    silence_tensorflow()
    import tensorflow as tf

    ...

    # your code

Can it be done within the import?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Sure, you can do everything with a single line by
importing the submodule auto:

.. code:: python

    import silence_tensorflow.auto
    import tensorflow as tf

    ...

    # your code

How can I get pylint to ignore the unused import?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You can use the flag 'disable=unused-import' as such:

.. code:: python

    import silence_tensorflow.auto  # pylint: disable=unused-import
    import tensorflow as tf

    ...

    # your code

How can I get pylint to ignore the unused variable?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you import silence_tensorflow in the context of a function
you will get a different warning from pyling: unused variable.
You can use the flag 'disable=unused-variable' as such:

.. code:: python
    
    def func():
        import silence_tensorflow.auto  # pylint: disable=unused-variable
        import tensorflow as tf

        ...

        # your code

How does this work under the hood?
----------------------------------------
This package will set the `KMP_AFFINITY` system variable to `"noverbose"`,
`TF_CPP_MIN_LOG_LEVEL` to level `3` (only errors logged).

If you need a custom value for `KMP_AFFINITY` you should reset it after importing the package, as follows:

.. code:: python

    import os
    from silence_tensorflow import silence_tensorflow
    backup = os.environ["KMP_AFFINITY"]
    silence_tensorflow()
    os.environ["KMP_AFFINITY"] = backup

.. |pip| image:: https://badge.fury.io/py/silence-tensorflow.svg
    :target: https://badge.fury.io/py/silence-tensorflow
    :alt: Pypi project

.. |downloads| image:: https://pepy.tech/badge/silence-tensorflow
    :target: https://pepy.tech/badge/silence-tensorflow
    :alt: Pypi total project downloads 