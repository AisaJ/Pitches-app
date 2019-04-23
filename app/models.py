from . import db
from datetime import datetime

class Pitch(db.Model):
  '''
  Class to define pitch objects
  '''
  __tablename__ = 'pitches'

  id = db.Column(db.Integer,primary_key=True)
  pitch = db.Column(db.String(255))
  category = db.Column(db.String(255))
  name = db.Column(db.String(255))
  vote_count = db.Column(db.Integer)
  added_date = db.Column(db.DateTime,default=datetime.utcnow)