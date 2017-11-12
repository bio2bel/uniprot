# -*- coding: utf-8 -*-

import pyuniprot
from pybel.constants import NAMESPACE_DOMAIN_GENE
from pybel.resources.arty import get_today_arty_namespace
from pybel.resources.definitions import write_namespace
from pybel.resources.deploy import deploy_namespace

MODULE_NAME = 'uniprot'


def iterate_accessions():
    """Iterates over uniprot accessions

    For example: ``P62258``, ``B3KY71``, and ``D3DTH5``

    :return: An iterator over the UniProt acessions
    :rtype: iter[str]
    """
    query = pyuniprot.query()

    all_accessions = query.get_accession()

    query.get_entry()
    for accession in all_accessions:
        yield accession.accession


def write_uniprot_belns(file):
    """Writes the UniProt accession BEL namespaces to a file

    :param file file: A write-enabled file or file-like
    """
    values = iterate_accessions()

    write_namespace(
        namespace_name='UniProt',
        namespace_keyword='UNIPROT',
        namespace_domain=NAMESPACE_DOMAIN_GENE,
        author_name='Charles Tapley Hoyt',
        author_contact='charles.hoyt@scai.fraunhofer.de',
        author_copyright='Creative Commons by 4.0',
        citation_name='UniProt Knowledge Base',
        values=values,
        functions='P',
        file=file
    )


def deploy_to_arty():
    """Gets the data and writes BEL namespace file to artifactory

    :return: The resource path, if it was deployed successfully, else none.
    :rtype: str
    """
    file_name = get_today_arty_namespace(MODULE_NAME)

    with open(file_name, 'w') as file:
        write_uniprot_belns(file)

    return deploy_namespace(file_name, MODULE_NAME)
