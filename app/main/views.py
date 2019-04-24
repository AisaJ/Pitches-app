from . import main
from flask import render_template,request,redirect,url_for,abort,flash
from ..models import Pitch,User
from flask_login import login_required,current_user
from .forms import PitchForm,UpdateProfile
from .. import db


@main.route('/')
def index():

  title = 'What can 30 seconds do for you?'  

  return render_template('index.html',title = title)

@main.route('/pitch/new',methods = ['GET','POST'])
@login_required
def new_pitch():
  form = PitchForm()

  if form.validate_on_submit():
    title=form.title.data
    category = form.category.data
    pitch = form.pitch.data
    author = current_user
    new_pitch = Pitch(title=title,category=category,pitch=pitch,author=current_user._get_current_object().id)

    db.session.add(new_pitch)
    db.session.commit()

    flash('Awesome! Pitch created','success')
    return redirect(url_for('main.new_pitch',id=new_pitch.id))

  pitches = Pitch.query.all()
  return render_template('pitch.html',title='new pitch',pitch_form=form, pitches=pitches)

@main.route('/user/<uname>')
def profile(uname):
  user = User.query.filter_by(username=uname).first()

  if user is None:
    abort(404)

  return render_template('profile/profile.html',user=user)

@main.route('/user/<uname>/update',methods=['GET','POST'])
@login_required
def update_profile(uname):
  user = User.query.filter_by(username=uname).first()

  if user is None:
    abort (404)
  form = UpdateProfile()

  if form.validate_on_submit():
    user.bio = form.bio.data

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('.profile',uname=user.username))

  return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods=['POST'])
@login_required
def update_pic(uname):
  user = User.query.filter_by(username=uname).first()
  if 'photo' in request.files:
    filename = photos.save(request.files['photo'])
    path = f'photos/{filename}'
    user.profile_pic_path = path
    db.session.commit()

  return redirect(url_for('main.profile',uname=uname))