from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
class RegistrationForm(FlaskForm):
    name = StringField('Nutzer-Name', validators=[DataRequired(), Length(3,10, message="Zwischen 3 & 10 Zeichen")])
    email = StringField('Nutzer-Email', validators=[DataRequired(),Email()])
    passwort = PasswordField('Passwort', validators=[DataRequired(), Length(8), EqualTo('confirm_pw'),] )
    confirm_pw = PasswordField('Confirm', validators=[DataRequired()])
    submit = SubmitField('Anmelden')