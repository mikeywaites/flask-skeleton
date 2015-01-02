#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
db.session = db.create_scoped_session({'autoflush': False})


from . auth import User  # NOQA
