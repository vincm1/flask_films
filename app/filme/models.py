from email.mime import image
from app import db
from datetime import datetime

class Film(db.Model):
    __tablename__ = 'film'

    id = db.Column(db.Integer, primary_key = True)
    titel = db.Column(db.String, index=True, nullable=False, unique=True)
    laenge = db.Column(db.Float)
    regie = db.Column(db.String)
    preise = db.Column(db.String)
    jahr = db.Column(db.Integer)
    schauspieler = db.Column(db.String)
    rating = db.Column(db.Float)
    image = db.Column(db.String(100), unique=True, nullable=False)
    

    def __init__(self, titel, laenge, regie, preise, jahr, schauspieler, rating, image):
        self.titel = titel
        self.laenge = laenge
        self.regie = regie
        self.preise = preise
        self.jahr = jahr
        self.schauspieler = schauspieler
        self.rating = rating
        self.image = image

    def __repr__(self):
        return "Filmname ist {}".format(self.titel)