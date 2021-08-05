
import os


#-------------- App Config --------------

APP_DEBUG = os.environ.get('APP_DEBUG')


#--------------- JWT Config --------------
JWT_SECRET = os.environ.get('JWT_SECRET')
JWT_REF_SECRET = os.environ.get('JWT_REF_SECRET')


#----------- Mongodb Config --------------

MONGO_HOST = os.environ.get('MONGO_HOST')
MONGO_PORT = os.environ.get('MONGO_PORT')
MONGO_DB = os.environ.get('MONGO_DB')
MONGO_USERNAME = os.environ.get('MONGO_USERNAME')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD')


#------------ Mail Config ----------------


MAIL_SERVER = os.environ.get('MAIL_SERVER')
MAIL_PORT = os.environ.get('MAIL_PORT')
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL')
