#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint

api_mod = Blueprint('api', __name__)


@api_mod.route('/')
def home():

    return {'foo': 'bar'}, 200
