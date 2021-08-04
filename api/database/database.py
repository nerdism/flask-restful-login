#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_mongoengine import MongoEngine


db = MongoEngine()


def create_db(app):
    db = MongoEngine(app)
    


