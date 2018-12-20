from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from FlaskSite.Models import  User
from FlaskSite.Variables import *


class inputData(FlaskForm):
    nama = StringField('Nama', validators=[DataRequired()])
    rokok = BooleanField('Smoking')
    alkohol = BooleanField('Alcohol')
    formal = BooleanField('Formal')