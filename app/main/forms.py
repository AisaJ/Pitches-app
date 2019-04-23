from flask_wtf import FlaskForm
from wtforms import SelectField,TextAreaField,SubmitField,StringField
from wtforms.validators import required

class CategoryForm(FlaskForm):

  category = SelectField('category_id')
