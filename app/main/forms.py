from flask_wtf import FlaskForm
from wtforms import SelectField,TextAreaField,SubmitField,StringField
from wtforms.validators import Required

class PitchForm(FlaskForm):

  title = StringField('Pitch title')
  category = SelectField("Choose Category",choices=[('Personal Brand','personal brand'),('Product','product'),('Project','project'),('Investor','investor')])
  pitch = TextAreaField('Your Pitch',validators=[Required()])
  submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
  bio =TextAreaField('Short description about you.',validators=[Required()])
  submit = SubmitField('Submit ')