# -*- coding: utf-8 -*-

"""Manager for Bio2BEL UniProt."""

from pybel import BELGraph
from .parser import get_mappings_df

__all__ = [
    'Manager',
]


class Manager:
    """Manager for UniProt."""

    def __init__(self):  # noqa: D107
        self.mappings_df = get_mappings_df()

    def normalize_terms(self, graph: BELGraph):
        """Normalize UniProt proteins in the graph."""
