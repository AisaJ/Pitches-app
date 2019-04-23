from . import main
from flask import render_template
from ..models import Pitch


@main.route('/')
def index():

  title = 'What can 30 seconds do for you?'

  return render_template('index.html',title = title)