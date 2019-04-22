import os
class Config:
  '''
  General configuration parent class
  '''
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:jemila@localhost/pitches'

class ProdConfig(Config):
  pass


class TestConfig(Config):
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class DevConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:jemila@localhost/watchlist'
  DEBUG = True

config_options = {
  'development':DevConfig,
  'production':ProdConfig,
  'test':TestConfig
}