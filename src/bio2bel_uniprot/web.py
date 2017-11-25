# -*- coding: utf-8 -*-

""" This module contains the flask application to visualize the db"""

import flask_admin
from flask import Flask
from flask_admin.contrib.sqla import ModelView

from pyuniprot.manager.database import DbManager
from pyuniprot.manager.models import *


def add_admin(app, session, url=None):
    admin = flask_admin.Admin(app, url=(url or '/'))
    admin.add_view(ModelView(Entry, session))
    admin.add_view(ModelView(OtherGeneName, session))
    admin.add_view(ModelView(Sequence, session))
    admin.add_view(ModelView(Version, session))
    admin.add_view(ModelView(Disease, session))
    admin.add_view(ModelView(DiseaseComment, session))
    admin.add_view(ModelView(Pmid, session))
    admin.add_view(ModelView(OrganismHost, session))
    admin.add_view(ModelView(DbReference, session))
    admin.add_view(ModelView(Feature, session))
    admin.add_view(ModelView(Function, session))
    admin.add_view(ModelView(Keyword, session))
    admin.add_view(ModelView(ECNumber, session))
    admin.add_view(ModelView(SubcellularLocation, session))
    admin.add_view(ModelView(TissueSpecificity, session))
    admin.add_view(ModelView(TissueInReference, session))
    return admin


def create_app(connection=None, url=None):
    """Creates a Flask application

    :type connection: Optional[str]
    :rtype: flask.Flask
    """
    app = Flask(__name__)
    manager = DbManager(connection=connection)
    add_admin(app, manager.session, url=url)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
