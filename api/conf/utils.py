import logging

from flask_bcrypt import Bcrypt
from flask_mail import Mail, Message
from flask import current_app, g



class Utils:

    def init_bcrypt(self, app):
        self.kb_bcrypt = Bcrypt(app)

    @property
    def get_bcrypt(self):
        return self.kb_bcrypt

    def init_mail(self, app):
        self.kb_mail = Mail(app)

    @property
    def get_mail(self):
        return self.kb_mail


    def send_mail(self, msg):
        with current_app.app_context():
            self.kb_mail.send(msg)

    
    
utils = Utils()



