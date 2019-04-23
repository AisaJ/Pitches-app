from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_bootstrap import Bootstrap

db = SQLAlchemy()

def create_app(config_name):
  app = Flask(__name__)

  #creating app configurations
  app.config.from_object(config_options[config_name])

  #Registering blueprint
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

  #Initializing flask extensions
  db.init_app(app)
  bootstrap = Bootstrap(app)

  return app