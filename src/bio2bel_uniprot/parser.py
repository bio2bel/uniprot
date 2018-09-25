# -*- coding: utf-8 -*-

"""Downloading and parsing functions for Bio2BEL UniProt."""

from bio2bel.downloading import make_df_getter
from .constants import MAPPINGS_PATH, MAPPINGS_URL

get_mappings_df = make_df_getter(MAPPINGS_URL, MAPPINGS_PATH, sep='\t')
"""Returns a file with the following columns:
1. UniProtKB-AC
2. UniProtKB-ID
3. GeneID (EntrezGene)
4. RefSeq
5. GI
6. PDB
7. GO
8. UniRef100
9. UniRef90
10. UniRef50
11. UniParc
12. PIR
13. NCBI-taxon
14. MIM
15. UniGene
16. PubMed
17. EMBL
18. EMBL-CDS
19. Ensembl
20. Ensembl_TRS
21. Ensembl_PRO
22. Additional PubMed
"""

SLIM_COLUMNS = ['UniProtKB-AC', 'UniProtKB-ID', 'GeneID', 'NCBI-Taxon']
get_slim_mappings_df = make_df_getter(MAPPINGS_URL, MAPPINGS_PATH, sep='\t', usecols=[0, 1, 2, 12], names=SLIM_COLUMNS)
