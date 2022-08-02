from datetime import datetime
from email.policy import default
from app import db, bcrypt

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), unique=True, nullable=False)
    user_email = db.Column(db.String(100), unique=True)
    user_password = db.Column(db.String(80))
    registration_date = db.Column(db.DateTime, default=datetime.now)

    # classmethods gehören zu einer Klasse, aber sind nicht verbunden mit Class Instanzen
    @classmethod
    def create_user(cls, user, email, password):
        user = cls(user_name=user,
                    user_email=email,
                    user_password=bcrypt.generate_password_hash(password).decode('utf-8'))
        
        db.session.add(user)
        db.session.commit
        return user