#!/usr/bin/python
# -*- coding: utf-8 -*-

from passlib.hash import bcrypt

from .base import db, BaseMixin


class User(db.Model, BaseMixin):
    __tablename__ = 'users'

    name = db.Column(db.String(300), nullable=False)
    email = db.Column(db.String(300), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def set_password(self, password, rounds=12):
        """Hash a plain text password and set the encrypted version against
        this instance.
        :param password: hashable str
        :param rounds: Specify the number of rounds bcrypt will perform
        :returns: None
        """
        self.password = bcrypt.encrypt(password, rounds=rounds)

    def verify_password(self, password):
        """Verify an encrypted password using ``password`` as a salt.
        :param password: hashable str
        :returns: True when valid, false otherwise
        """

        if not self.password:
            return False
        return bcrypt.verify(password, self.password)
