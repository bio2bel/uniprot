Bio2BEL UniProt |build| |coverage| |docs| |zenodo|
==================================================
Converts UniProt to BEL

Installation |pypi_version| |python_versions| |pypi_license|
------------------------------------------------------------
``bio2bel_uniprot`` can be installed easily from `PyPI <https://pypi.python.org/pypi/bio2bel_uniprot>`_ with
the following code in your favorite terminal:

.. code-block:: sh

    $ python3 -m pip install bio2bel_uniprot

or from the latest code on `GitHub <https://github.com/bio2bel/uniprot>`_ with:

.. code-block:: sh

    $ python3 -m pip install git+https://github.com/bio2bel/uniprot.git@master

Setup
-----
uniprot can be downloaded and populated from either the Python REPL or the automatically installed command line
utility.

Python REPL
~~~~~~~~~~~
.. code-block:: python

    >>> import bio2bel_uniprot
    >>> uniprot_manager = bio2bel_uniprot.Manager()
    >>> uniprot_manager.populate()

Command Line Utility
~~~~~~~~~~~~~~~~~~~~
.. code-block:: bash

    bio2bel_uniprot populate


.. |build| image:: https://travis-ci.org/bio2bel/uniprot.svg?branch=master
    :target: https://travis-ci.org/bio2bel/uniprot
    :alt: Build Status

.. |coverage| image:: https://codecov.io/gh/bio2bel/uniprot/coverage.svg?branch=master
    :target: https://codecov.io/gh/bio2bel/uniprot?branch=master
    :alt: Coverage Status

.. |docs| image:: http://readthedocs.org/projects/bio2bel-uniprot/badge/?version=latest
    :target: http://bio2bel.readthedocs.io/projects/uniprot/en/latest/?badge=latest
    :alt: Documentation Status

.. |climate| image:: https://codeclimate.com/github/bio2bel/uniprot/badges/gpa.svg
    :target: https://codeclimate.com/github/bio2bel/uniprot
    :alt: Code Climate

.. |python_versions| image:: https://img.shields.io/pypi/pyversions/bio2bel_uniprot.svg
    :alt: Stable Supported Python Versions

.. |pypi_version| image:: https://img.shields.io/pypi/v/bio2bel_uniprot.svg
    :alt: Current version on PyPI

.. |pypi_license| image:: https://img.shields.io/pypi/l/bio2bel_uniprot.svg
    :alt: MIT License

.. |zenodo| image:: https://zenodo.org/badge/97003706.svg
    :target: https://zenodo.org/badge/latestdoi/97003706
    :alt: Zenodo DOI