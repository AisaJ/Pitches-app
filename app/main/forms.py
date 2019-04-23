from flask_wtf import FlaskForm
from wtforms import SelectField,TextAreaField,SubmitField,StringField
from wtforms.validators import required

class PitchForm(FlaskForm):

  title = StringField('Pitch title')
  category = SelectField("Choose Category",choices=[('Personal Brand','personal brand'),('Product','product'),('Project','project'),('Investor','investor')])
  review = TextAreaField('Your Pitch',validators=[Required()])
  name = StringField('Preferred name')
  submit = SubmitField('Submit')