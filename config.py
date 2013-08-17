class Config(object):
    DEBUG = False
    TESTING = False

class Development(Config):
    DEBUG = True
    DATABASE = 'development_db'

class Production(Config):
    DATABASE = 'production_db'
