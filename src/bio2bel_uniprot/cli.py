# -*- coding: utf-8 -*-

"""Run this script with either :code:`python3 -m bio2bel_uniprot arty`"""

from __future__ import print_function

import logging
import sys

import click

from .constants import DEFAULT_CACHE_CONNECTION
from .manager import Manager
from .run import deploy_to_arty, write_uniprot_belns


@click.group()
def main():
    """UniProt to BEL"""
    logging.basicConfig(level=10, format="%(asctime)s - %(levelname)s - %(message)s")


@main.command()
@click.option('-c', '--connection', help="Defaults to {}".format(DEFAULT_CACHE_CONNECTION))
@click.option('-o', '--output', type=click.File('w'), default=sys.stdout)
def write(connection, output):
    """Writes the UniProt accession name space"""
    write_uniprot_belns(output, connection=connection)


@main.command()
@click.option('-c', '--connection', help="Defaults to {}".format(DEFAULT_CACHE_CONNECTION))
def deploy(connection):
    """Deploy to Artifactory"""
    success = deploy_to_arty(connection=connection)
    click.echo('Deployed to {}'.format(success) if success else 'Duplicate not deployed')


@main.command()
@click.option('-c', '--connection', help="Defaults to {}".format(DEFAULT_CACHE_CONNECTION))
@click.option('-t', '--tax-id', default=['9606'], multiple=True,
              help='Keep this taxonomy identifier. Can specify multiple. Defaults to just human.')
def populate(connection, tax_id):
    """Populate the database"""
    manager = Manager(connection=connection)
    manager.populate(taxids=tax_id)
    manager.session.close()


if __name__ == '__main__':
    main()
