from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Optiona
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class UserForm(FlaskForm):
    username = StringField('Nazwa Użytkownika', validators=[DataRequired(), Length(min=2, max=80)])
    email = StringField('Email', validators=[DataRequired(), Length(max=120)])
    submit = SubmitField('Zapisz Użytkownika')

class UserForm(FlaskForm):
    username = StringField('Nazwa Użytkownika', validators=[DataRequired(), Length(min=2, max=80)])
    email = StringField('Email', validators=[DataRequired(), Length(max=120)])
    submit = SubmitField('Zapisz Użytkownika')

class TaskForm(FlaskForm):
    title = StringField('Tytuł Zadania', validators=[DataRequired(), Length(min=5, max=100)])
    description = TextAreaField('Opis', validators=[Optional()])
    is_completed = BooleanField('Ukończone')
    user_id = IntegerField('ID Użytkownika', validators=[DataRequired()])
    submit = SubmitField('Zapisz Zadanie')