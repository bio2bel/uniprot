# -*- coding: utf-8 -*-

"""Run this script with either :code:`python3 -m bio2bel_uniprot arty`"""

from __future__ import print_function

import logging
import sys

import click
import pyuniprot

from .run import deploy_to_arty, write_uniprot_belns


@click.group()
def main():
    """UniProt to BEL"""
    logging.basicConfig(level=10, format="%(asctime)s - %(levelname)s - %(message)s")


@main.command()
def update():
    """Update PyUniProt data"""
    pyuniprot.update()


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


if __name__ == '__main__':
    main()
