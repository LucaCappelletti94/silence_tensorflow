silence_tensorflow
=========================================================================================
|travis| |sonar_quality| |sonar_maintainability|
|codacy| |code_climate_maintainability| |pip| |downloads|

Simple python package to shut up Tensorflow warnings and logs.

How do I install this package?
----------------------------------------------
As usual, just download it using pip:

.. code:: shell

    pip install silence_tensorflow

Tests Coverage
----------------------------------------------
Since some software handling coverages sometimes
get slightly different results, here's three of them:

|coveralls| |sonar_coverage| |code_climate_coverage|

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

.. |travis| image:: https://travis-ci.org/LucaCappelletti94/silence_tensorflow.png
   :target: https://travis-ci.org/LucaCappelletti94/silence_tensorflow
   :alt: Travis CI build

.. |sonar_quality| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_silence_tensorflow&metric=alert_status
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_silence_tensorflow
    :alt: SonarCloud Quality

.. |sonar_maintainability| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_silence_tensorflow&metric=sqale_rating
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_silence_tensorflow
    :alt: SonarCloud Maintainability

.. |sonar_coverage| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_silence_tensorflow&metric=coverage
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_silence_tensorflow
    :alt: SonarCloud Coverage

.. |coveralls| image:: https://coveralls.io/repos/github/LucaCappelletti94/silence_tensorflow/badge.svg?branch=master
    :target: https://coveralls.io/github/LucaCappelletti94/silence_tensorflow?branch=master
    :alt: Coveralls Coverage

.. |pip| image:: https://badge.fury.io/py/silence-tensorflow.svg
    :target: https://badge.fury.io/py/silence-tensorflow
    :alt: Pypi project

.. |downloads| image:: https://pepy.tech/badge/silence-tensorflow
    :target: https://pepy.tech/badge/silence-tensorflow
    :alt: Pypi total project downloads 

.. |codacy| image:: https://api.codacy.com/project/badge/Grade/e6fe64db1c9042bbaa4c0a20bde585dc
    :target: https://www.codacy.com/app/LucaCappelletti94/silence_tensorflow?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=LucaCappelletti94/silence_tensorflow&amp;utm_campaign=Badge_Grade
    :alt: Codacy Maintainability

.. |code_climate_maintainability| image:: https://api.codeclimate.com/v1/badges/c2c6e147021b6855351e/maintainability
    :target: https://codeclimate.com/github/LucaCappelletti94/silence_tensorflow/maintainability
    :alt: Maintainability

.. |code_climate_coverage| image:: https://api.codeclimate.com/v1/badges/c2c6e147021b6855351e/test_coverage
    :target: https://codeclimate.com/github/LucaCappelletti94/silence_tensorflow/test_coverage
    :alt: Code Climate Coverate
