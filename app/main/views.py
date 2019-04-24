from . import main
from flask import render_template,request,redirect,url_for,abort
from ..models import Pitch,User
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
    category = form.category.data
    pitch = form.pitch.data
    author = form.author.data

    db.session.add(pitch)
    db.session.commit()

    flash('Awesome! Pitch created','success')
    return redirect(url_for('main.index',id=pitch.id))

  return render_template('pitch.html',title='new pitch',pitch_form=form, post='new pitch')

@main.route('/user/<uname>')
def profile(uname):
  user = User.query.filter_by(username=uname).first()

  if user is None:
    abort(404)

  return render_template('profile/profile.html',user=user)
