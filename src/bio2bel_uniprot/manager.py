# -*- coding: utf-8 -*-

import pyuniprot
from bio2bel import AbstractManager, get_connection
from pyuniprot.manager.models import *
from pyuniprot.manager.query import QueryManager
from .constants import MODULE_NAME


def _get_connection_string(connection):
    return get_connection(module_name=MODULE_NAME, connection=connection)


# Monkey patch PyUniProt connection loader
pyuniprot.manager.database.get_connection = _get_connection_string


def _deal_with_nonsense(results):
    if not results:
        return

    if 1 < len(results):
        raise ValueError

    return results[0]


class _PyUniProtManager(QueryManager):
    pass


class Manager(AbstractManager, _PyUniProtManager):
    module_name = MODULE_NAME
    flask_admin_models = [Entry, Disease]

    def populate(self, *args, **kwargs):
        """Updates the CTD database
        
        1. downloads gzipped XML
        2. drops all tables in database
        3. creates all tables in database
        4. import XML
        5. close session

        :param list[str] taxids: list of NCBI taxonomy identifier
        :param iter[str] url: iterable of URL strings
        :param bool force_download: force method to download
        """
        self.db_import_xml(*args, **kwargs)

    def get_protein_by_uniprot_id(self, uniprot_id):
        """Gets a UniProt entry by its identifier

        :param str uniprot_id:
        :rtype: Optional[pyuniprot.manager.models.Entry]
        """
        results = self.entry(name=uniprot_id)
        return _deal_with_nonsense(results)
