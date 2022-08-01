from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired


class AddFilmForm(FlaskForm):
    titel = StringField('Titel', validators=[DataRequired()])
    laenge = FloatField('Spiellänge', validators=[DataRequired()])
    regie = StringField('Regie', validators=[DataRequired()])
    jahr = IntegerField('Jahr der Veröffentlichung', validators=[DataRequired()])
    image = StringField('Cover', validators=[DataRequired()])
    schauspieler = StringField('Besetzung', validators=[DataRequired()])
    rating = FloatField('Imdb Rating', validators=[DataRequired()])
    preise = StringField('Oscars, Grammys etc.', validators=[DataRequired()])
    submit = SubmitField('Hinzufügen')
class EditFilmForm(FlaskForm):
    titel = StringField('Titel', validators=[DataRequired()])
    laenge = FloatField('Spiellänge', validators=[DataRequired()])
    regie = StringField('Regie', validators=[DataRequired()])
    jahr = IntegerField('Jahr der Veröffentlichung', validators=[DataRequired()])
    image = StringField('Cover', validators=[DataRequired()])
    schauspieler = StringField('Besetzung', validators=[DataRequired()])
    rating = FloatField('Imdb Rating', validators=[DataRequired()])
    preise = StringField('Oscars, Grammys etc.', validators=[DataRequired()])
    submit = SubmitField('Update')