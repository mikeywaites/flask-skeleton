#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify

api_mod = Blueprint('api', __name__)


@api_mod.route('/')
def home():

    return jsonify({'foo': 'bar'}), 200
