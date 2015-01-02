#!/usr/bin/python
# -*- coding: utf-8 -*-

import arrow

from . import db

utc_now = lambda x: arrow.utcnow().datetime


class PrimaryKeyMixin(object):

    id = db.Column(db.Integer, primary_key=True)


class CreatedUpdatedMixin(object):

    created_at = db.Column(db.DateTime, default=utc_now, nullable=False)
    updated_at = db.Column(
        db.DateTime, default=utc_now,
        onupdate=utc_now, nullable=False)

    # hack to move the timestamp columns to the end
    created_at._creation_order = 9998
    updated_at._creation_order = 9999


class BaseMixin(PrimaryKeyMixin, CreatedUpdatedMixin):
    pass
