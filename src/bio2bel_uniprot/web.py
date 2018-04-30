# -*- coding: utf-8 -*-

""" This module contains the flask application to visualize the db"""

from pyuniprot.manager.models import *
from .manager import Manager


def add_admin(app, session, **kwargs):
    import flask_admin
    from flask_admin.contrib.sqla import ModelView
    admin = flask_admin.Admin(app, **kwargs)
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


if __name__ == '__main__':
    manager = Manager()
    app = manager.get_flask_admin_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
