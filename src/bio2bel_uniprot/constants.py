# -*- coding: utf-8 -*-

from os import environ, makedirs, path

MODULE_NAME = 'uniprot'
#: The default directory where PyBEL files, including logs and the  default cache, are stored. Created if not exists.
BIO2BEL_DIR = environ.get('BIO2BEL_DIRECTORY', path.join(path.expanduser('~'), '.pybel', 'bio2bel'))
DATA_DIR = path.join(BIO2BEL_DIR, MODULE_NAME)
makedirs(DATA_DIR, exist_ok=True)

DEFAULT_CACHE_NAME = '{}.db'.format(MODULE_NAME)
DEFAULT_CACHE_LOCATION = path.join(DATA_DIR, DEFAULT_CACHE_NAME)
DEFAULT_CACHE_CONNECTION = environ.get('BIO2BEL_CONNECTION', 'sqlite:///' + DEFAULT_CACHE_LOCATION)
