from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.auth.models import User

def check_name(form, field):
    name = User.query.filter_by(user_name=field.data).first()
    if name:
        raise ValidationError('Nutzername bereits vorhanden!')

def check_email(form, field):
    email = User.query.filter_by(user_email=field.data).first()
    if email:
        raise ValidationError('Email bereits vorhanden!')

class RegistrationForm(FlaskForm):
    name = StringField('Nutzer-Name', validators=[DataRequired(), Length(3,10, message="Zwischen 3 & 10 Zeichen"), check_name])
    email = StringField('Nutzer-Email', validators=[DataRequired(),Email(), check_email])
    passwort = PasswordField('Passwort', validators=[DataRequired(), Length(8), EqualTo('confirm_pw'),] )
    confirm_pw = PasswordField('Confirm', validators=[DataRequired()])
    submit = SubmitField('Anmelden')

class LoginForm(FlaskForm):
    email = StringField('Nutzer-Email', validators=[DataRequired(), Email()])
    passwort = PasswordField('Passwort', validators=[DataRequired()])
    submit = SubmitField('Anmelden')

