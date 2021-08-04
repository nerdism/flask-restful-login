#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime

from flask import g

from api.conf.auth import auth, jwt
#from api.database.database import db
from mongoengine import Document
from mongoengine import DateTimeField, StringField, ListField


class User(Document):


    # User email address.
    email = StringField(max_length=80, required=True, unique=True)

    # User Password

    password = StringField(max_length=80, required=True)

    refresh_token = StringField()

    note_url = StringField()

    md_url = StringField()

    cards_url = StringField()

    last_modified = DateTimeField(default=datetime.utcnow)

    # Generates auth token.
    def generate_auth_token(self):

        # Generate admin token with flag 1.
        token = jwt.dumps({"email": self.email})

        return token


    # Generates a new access token from refresh token.
    @staticmethod
    @auth.verify_token
    def verify_auth_token(token):

        # Create a global none user.
        g.user = None

        try:
            # Load token.
            data = jwt.loads(token)

        except:
            # If any error return false.
            return False

        # Check if email and admin permission variables are in jwt.
        if "email" in data:

            # Set email from jwt.
            g.user = data["email"]

            # Return true.
            return True

        # If does not verified, return false.
        return False

    def __repr__(self):
        return "User[email={}, refresh_token={}]".format(self.email, self.refresh_token)
    
    def __str__(self):
        return "User[email={}, refresh_token={}]".format(self.email, self.refresh_token)

"""
class Blacklist(db.Model):

    # Generates default class name for table. For changing use
    # __tablename__ = 'users'

    # Blacklist id.
    id = db.Column(db.Integer, primary_key=True)

    # Blacklist invalidated refresh tokens.
    refresh_token = db.Column(db.String(length=255))

    def __repr__(self):

        # This is only for representation how you want to see refresh tokens after query.
        return "<User(id='%s', refresh_token='%s', status='invalidated.')>" % (
            self.id,
            self.refresh_token,
        )
"""
