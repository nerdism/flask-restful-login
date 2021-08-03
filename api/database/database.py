#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_mongoengine import MongoEngine


db = None


def create_db(app):
    db = MongoEngine(app)
    


