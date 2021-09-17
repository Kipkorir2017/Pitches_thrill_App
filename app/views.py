from flask import render_template
from app import app


#views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title='Pitches Thrills'
    return render_template('index.html',title=title)

@app.route('/category/sports')
def sports():
    '''
    view function to display sports pitches
    '''
    sports_title ='sports Pitches'
    return render_template('pitches/sports.html',title=sports_title)

@app.route('/category/business')
def business():
    '''
    view function to display business pitches
    '''
    business_title='Business Pitches'
    return render_template('pitches/business.html',title=business_title)


@app.route('/category/interview')
def interview():
    '''
    view function to display interview pitches
    '''
    interview_title ='Interview Pitches'
    return render_template('pitches/interview.html',title=interview_title)

@app.route('/category/love')
def love():
    '''
    view function to display love pitches
    '''
    love_title='Love Pitches'
    return render_template('pitches/love.html',title=love_title)


@app.route('/category/study')
def study():
    '''
    view function to display study pitches
    '''
    study_title='Study Pitches'
    return render_template('pitches/study.html',title=study_title)


@app.route('/category/politics')
def politics():
    '''
    view function to display business pitches
    '''
    politics_title = 'Politics Pitches'
    return render_template('pitches/politics.html',title=politics_title)