import os


class BaseConfig(object):
    DEBUG  = False
    TESTING = False
    SECRET_KEY = os.urandom(16)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
