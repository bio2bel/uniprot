# -*- coding: utf-8 -*-

"""Manager for Bio2BEL UniProt."""

import logging
from typing import Iterable, Tuple

import networkx as nx
from pybel import BELGraph
from pybel.dsl import BaseEntity, Protein
from tqdm import tqdm

from .parser import get_slim_mappings_df

__all__ = [
    'Manager',
]

logger = logging.getLogger(__name__)


class Manager:
    """UniProt nomenclature."""

    def __init__(self, *args, **kwargs):
        self._mapping = None
        self._accession_to_identifier = None
        self._identifier_to_accession = None

    @property
    def mapping(self):
        if self._mapping is None:
            self._mapping = get_slim_mappings_df()
        return self._mapping

    @property
    def accession_to_identifier(self):
        if self._accession_to_identifier is None:
            self._accession_to_identifier = dict(self.mapping[['UniProtKB-AC', 'UniProtKB-ID']].values)
        return self._accession_to_identifier

    @property
    def identifier_to_accession(self):
        if self._identifier_to_accession is None:
            self._identifier_to_accession = dict(self.mapping[['UniProtKB-ID', 'UniProtKB-AC']].values)
        return self._identifier_to_accession

    def normalize_terms(self, graph: BELGraph, use_tqdm: bool = False) -> None:
        """Normalize UniProt entries."""
        nx.relabel_nodes(
            graph,
            dict(self.iter_proteins(graph, use_tqdm=use_tqdm)),
            copy=False,
        )

    def iter_proteins(self, graph: BELGraph, use_tqdm: bool = False) -> Iterable[Tuple[Protein, Protein]]:
        it = (
            tqdm(graph, desc='UniProt proteins')
            if use_tqdm else
            graph
        )
        for node in it:
            x = self.lookup_protein(node)
            if x is not None:
                yield node, x

    def lookup_protein(self, node: BaseEntity):
        if not isinstance(node, Protein):
            return
        namespace = node.namespace
        if not namespace or namespace.lower() not in {'uniprot', 'up'}:
            return
        identifier = node.identifier
        name = node.name
        if identifier and name:
            return
        if identifier:
            name = self.identifier_to_accession.get(identifier)
            if name is not None:
                return Protein(
                    namespace=namespace,
                    identifier=identifier,
                    name=name,
                    variants=node.variants,
                )
            name = self.accession_to_identifier.get(identifier)  # flip them!
            if name is not None:
                return Protein(
                    namespace=namespace,
                    identifier=name,
                    name=identifier,
                    variants=node.variants,
                )
            logger.warning(f'Can not find UniProt identifier: {identifier}')
            return
        if name:
            identifier = self.accession_to_identifier.get(name)
            if identifier is not None:
                return Protein(
                    namespace=namespace,
                    identifier=identifier,
                    name=name,
                    variants=node.variants,
                )
            identifier = self.identifier_to_accession.get(name)  # flip them!
            if identifier is not None:
                return Protein(
                    namespace=namespace,
                    identifier=name,
                    name=identifier,
                    variants=node.variants,
                )
            logger.warning(f'Can not find UniProt name: {name}')
