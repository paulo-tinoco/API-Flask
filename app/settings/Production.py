from .Base import BaseConfig


class ProductionConfig(BaseConfig):
    ENV = 'production'
    DEBUG = True
    TESTING = True
    VERSIONS = 1
    MODULES = [
        'users',
        'products',
    ]
