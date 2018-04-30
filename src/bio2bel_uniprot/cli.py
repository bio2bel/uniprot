# -*- coding: utf-8 -*-

"""Run this script with either :code:`python3 -m bio2bel_uniprot`"""

from .manager import Manager

main = Manager.get_cli()

if __name__ == '__main__':
    main()
