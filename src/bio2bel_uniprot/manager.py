# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from bio2bel.utils import get_connection
from pyuniprot.manager.database import DbManager
from pyuniprot.manager.query import QueryManager
from .constants import MODULE_NAME


def _deal_with_nonsense(results):
    if not results:
        return

    if 1 < len(results):
        raise ValueError

    return results[0]


class Manager(DbManager, QueryManager):
    def __init__(self, connection=None, echo=False):
        """
        :param str connection: SQLAlchemy
        :param bool echo: True or False for SQL output of SQLAlchemy engine
        """
        self.connection = get_connection(MODULE_NAME, connection)
        self.engine = create_engine(self.connection, echo=echo)

        self.sessionmaker = sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=True
        )
        self.session = scoped_session(self.sessionmaker)

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

    def drop_all(self):
        self._drop_tables()

    def get_protein_by_uniprot_id(self, uniprot_id):
        """Gets a UniProt entry by its identifier

        :param str uniprot_id:
        :rtype: Optional[pyuniprot.manager.models.Entry]
        """
        results = self.entry(name=uniprot_id)
        return _deal_with_nonsense(results)
