#!/usr/bin/python
# -*- coding: utf-8 -*-

from .base import db, BaseMixin


class User(db.Model, BaseMixin):

    __tablename__ = "users"

    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(300), unique=True)

    def __repr__(self):
        return self.name
