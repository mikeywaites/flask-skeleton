#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    An example models.py for use with {{PROJECT_NAME}}

    Useage::

        from {{PROJECT_NAME}}.database import db

        class FooModel(db.Model):

            __tablename__ = 'foos'

            id = db.Column(db.Integer, primary=True)
            name = db.Column(db.String(30), nullable=False)
"""

from {{PROJECT_NAME}}.database import db
