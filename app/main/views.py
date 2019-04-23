from . import main
from flask import render_template
from ..models import Pitch
from flask_login import login_required


@main.route('/')
def index():

  title = 'What can 30 seconds do for you?'
  pitches = Pitch.query.all()

  return render_template('index.html',title = title)

@main.route('/pitch/new',methods = ['GET','POST'])
@login_required
def new_pitch():
  form = PitchForm()

  if form.validate_on_submit():
    title=form.title.data

    db.session.add(pitch)
    db.session.commit()

    flash('Awesome! Pitch created','success')
    return redirect(url_for('main.index',id=pitch.id))

  return render_template('new_pitch.html',title='new pitch',pitch_form=form, post='new pitch')
