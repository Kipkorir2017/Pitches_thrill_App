from flask import render_template,redirect, url_for
# from app import app
from . import main
from wtforms import form
from .forms import PitchesForm
from ..models import Pitch
from flask_login import login_required

#views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title='Pitches Thrills'
    return render_template('index.html',title=title)


@main.route('/pitch/newpitch', methods=['POST', 'GET'])
@login_required
def new_pitch():
    form = PitchesForm()
    if form.validate_on_submit():
        pitch_title = form.pitch_title.data
        pitch_category = form.pitch_category.data
        pitch_comment = form.pitch_comment.data
       

        #update pitch instance
        new_pitch = Pitch(pitch_title,pitch_category,pitch_comment)
                          
                          

        #save pitch
        new_pitch.save_pitch()
        return redirect(url_for('.index'))

    title = 'Add New pitch'
    return render_template('pitches.html', title=title, pitchesform=form)



@main.route('/category/sports')
def sports():
    '''
    view function to display sports pitches
    '''
    pitches=Pitch.get_pitches('sports')
    sports_title ='sports Pitches'
    return render_template('pitches/sports.html',title=sports_title,sports_pitch=pitches)

@main.route('/category/business')
def business():
    '''
    view function to display business pitches
    '''
    pitches=Pitch.get_pitches('business')
    business_title='Business Pitches'
    return render_template('pitches/business.html',title=business_title,business_pitch=pitches)


@main.route('/category/interview')
def interview():
    '''
    view function to display interview pitches
    '''
    pitches=Pitch.get_pitches('interview')
    interview_title ='Interview Pitches'
    return render_template('pitches/interview.html',title=interview_title,interview_pitch=pitches)

@main.route('/category/love')
def love():
    '''
    view function to display love pitches
    '''
    pitches=Pitch.get_pitches('love')
    love_title='Love Pitches'
    return render_template('pitches/love.html',title=love_title, love_pitch=pitches)


@main.route('/category/study')
def study():
    '''
    view function to display study pitches
    '''
    pitches=Pitch.get_pitches('study')
    study_title='Study Pitches'
    return render_template('pitches/study.html',title=study_title,study_pitch=pitches)


@main.route('/category/politics')
def politics():
    '''
    view function to display business pitches
    '''
    pitches=Pitch.get_pitches('politics')
    politics_title = 'Politics Pitches'
    return render_template('pitches/politics.html',title=politics_title,politics_pitch=pitches)

