silence_tensorflow
========================================
|travis| |sonar_quality| |sonar_maintainability| |sonar_coverage| |code_climate_maintainability|

Simple python package to shut up Tensorflow warnings and logs. 

How do I get it?
----------------------------------------
As usual, just install it from pip:

.. code:: bash

    pip install silence_tensorflow

This package **WILL NOT** install Tensorflow with it, as often custom versions are needed for each setup.

How do I use it?
----------------------------------------
You only need to import the package before import Tensorflow:

.. code:: bash

    import silence_tensorflow
    import tensorflow as tf

    ...

    # your code

How does this work under the hood?
----------------------------------------
This package will set the `KMP_AFFINITY` system variable to `"noverbose"`, `TF_CPP_MIN_LOG_LEVEL` to level `2` (only errors logged) and silence both `FutureWarning` and `FutureWarning`.

If you need a custom value for `KMP_AFFINITY` you should reset it after importing the package, as follows:

.. code:: bash

    import os
    backup = os.environ["KMP_AFFINITY"]
    import silence_tensorflow
    os.environ["KMP_AFFINITY"] = backup


.. |travis| image:: https://travis-ci.org/LucaCappelletti94/silence_tensorflow.png
   :target: https://travis-ci.org/LucaCappelletti94/silence_tensorflow

.. |sonar_quality| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_silence_tensorflow&metric=alert_status
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_silence_tensorflow

.. |sonar_maintainability| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_silence_tensorflow&metric=sqale_rating
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_silence_tensorflow

.. |sonar_coverage| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_silence_tensorflow&metric=coverage
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_silence_tensorflow

.. |code_climate_maintainability| image:: https://api.codeclimate.com/v1/badges/25fb7c6119e188dbd12c/maintainability
   :target: https://codeclimate.com/github/LucaCappelletti94/silence_tensorflow/maintainability
   :alt: Maintainability
