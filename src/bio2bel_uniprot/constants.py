# -*- coding: utf-8 -*-

from os import environ, makedirs, path

#: The default directory where PyBEL files, including logs and the  default cache, are stored. Created if not exists.
BIO2BEL_DIR = environ.get('BIO2BEL_DIRECTORY', path.join(path.expanduser('~'), '.pybel', 'bio2bel'))
DATA_DIR = path.join(BIO2BEL_DIR, 'uniprot')
makedirs(DATA_DIR, exist_ok=True)

DEFAULT_CACHE_NAME = 'uniprot.db'
DEFAULT_CACHE_LOCATION = path.join(DATA_DIR, DEFAULT_CACHE_NAME)
DEFAULT_CACHE_CONNECTION = environ.get('BIO2BEL_CHEBI_DB', 'sqlite:///' + DEFAULT_CACHE_LOCATION)
