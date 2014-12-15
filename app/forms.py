from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class CreateEvent(Form):
    name    = StringField('name', validators=[DataRequired()])
    stub    = StringField('name', validators=[DataRequired()])
    game    = StringField('name', validators=[DataRequired()])
    stream  = StringField('name', validators=[DataRequired()])
    teams   = StringField('name', validators=[DataRequired()])
    twURL   = StringField('name', validators=[DataRequired()])
    twID    = StringField('name', validators=[DataRequired()])
    bracket = StringField('name', validators=[DataRequired()])

class CreateTeam(Form):
    name    = StringField('name', validators=[DataRequired()])

class CreatePlayer(Form):
    name    = StringField('name', validators=[DataRequired()])

class CreateGame(Form):
    name    = StringField('name', validators=[DataRequired()])

