import os
class Config:
  '''
  General configuration parent class
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:jemila@localhost/watchlist'
  '''
  SECRET_KEY = os.environ.get('SECRET_KEY')
  SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringaschool:jemila@localhost/pitches'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  UPLOADED_PHOTOS_DEST = 'app/static/photos'
 

class ProdConfig(Config):
  pass


class TestConfig(Config):
  pass
  # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class DevConfig(Config):
  DEBUG = True

config_options = {
  'development':DevConfig,
  'production':ProdConfig,
  'test':TestConfig
}