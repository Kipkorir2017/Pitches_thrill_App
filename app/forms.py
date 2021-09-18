from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class PitchesForm(FlaskForm):

    title = StringField('title',validators=[Required()])
    category = SelectField('Category',choices=[('Select category',
                                           'Select category'),
                                          ('sports', 'sports'),
                                          ('interview','interview'),
                                          ('business','Business'),
                                          ('love', 'love'),
                                          ('politics','Politics'),
                                          ('study','study')], validators=[Required()])
    comment = TextAreaField('new Pitch')
    submit = SubmitField('Submit')