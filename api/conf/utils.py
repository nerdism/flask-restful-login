from flask_bcrypt import Bcrypt


kb_bcrypt = Bcrypt()


def create_bcrypt(app):
    kb_bcrypt = Bcrypt(app)

