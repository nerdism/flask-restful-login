#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_mongoengine import MongoEngine



class Database:

    def init_db(self, app):
        self.db = MongoEngine(app)

    @property
    def get_db(self):
        return self.db




database = Database()
