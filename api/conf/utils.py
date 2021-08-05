import logging

from flask_bcrypt import Bcrypt
from flask_mail import Mail, Message
from flask import current_app, g


def init_bcrypt(app):
    if 'kb_bcrypt' not in g:
        g.kb_bcrypt = Bcrypt(app)


def get_bcrypt():
    if 'kb_bcrypt' in g:
        return g.kb_bcrypt
    logging.warn("kb_bcrypt is None in global object")
    return None 


def init_mail(app):
    if 'kb_mail' not in g:
        g.kb_mail = Mail(app)


def get_mail():
    if 'kb_mail' in g:
        return g.kb_mail

    logging.warn('kb_mail is None in global object')
    return None



def send_mail(msg):
    with current_app.app_context:
        g.kb_mail.send(msg)

    
    




