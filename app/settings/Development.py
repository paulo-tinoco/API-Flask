from .Base import BaseConfig


class DevelopmentConfig(BaseConfig):
    ENV = 'dev'
    DEBUG = True
    TESTING = True
    VERSIONS = 1
    MODULES = [
        'users',
        'products',
    ]
