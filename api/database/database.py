#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_mongoengine import MongoEngine
from flask import g

import logging



def init_db(app):
    if 'db' not in g:
        g.db = MongoEngine(app)


def get_db():
    if 'db' in g:
        return g.db
    logging.warn('db is None in global object')
    return None




