# -*- coding: utf-8 -*-

"""Run this script with either :code:`python3 -m bio2bel_uniprot arty`"""

from __future__ import print_function

import logging
import sys

import click

import pyuniprot
from .constants import DEFAULT_CACHE_CONNECTION
from .run import deploy_to_arty, write_uniprot_belns


@click.group()
def main():
    """UniProt to BEL"""
    logging.basicConfig(level=10, format="%(asctime)s - %(levelname)s - %(message)s")


@main.command()
@click.option('-o', '--output', type=click.File('w'), default=sys.stdout)
def write(output):
    """Writes the UniProt accession name space"""
    write_uniprot_belns(output)


@main.command()
def deploy():
    """Deploy to artifactory"""
    success = deploy_to_arty()
    click.echo('Deployed to {}'.format(success) if success else 'Duplicate not deployed')


@main.command()
@click.option('-c', '--connection', help="Defaults to {}".format(DEFAULT_CACHE_CONNECTION))
@click.option('-t', '--tax-id', help='Keep this taxonomy identifier. Can specify multiple', multiple=True)
def populate(connection, tax_id):
    """Populate the database"""
    pyuniprot.update(connection=connection, taxids=tax_id)


if __name__ == '__main__':
    main()
