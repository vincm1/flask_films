from datetime import datetime
from app import db, bcrypt
from flask_login import UserMixin
from app import login_manager

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    user_vornachname = db.Column(db.String(100), nullable=False)
    user_name = db.Column(db.String(20), unique=True, nullable=False)
    user_email = db.Column(db.String(100), unique=True)
    user_passwort = db.Column(db.String(80))
    registration_date = db.Column(db.DateTime, default=datetime.now)

    def check_passwort(self, passwort):
        return bcrypt.check_password_hash(self.user_passwort, passwort)

    # classmethods gehören zu einer Klasse, aber sind nicht verbunden mit Class Instanzen
    @classmethod
    def create_user(cls, user, email, vornachname, passwort):
        user = cls(user_name=user,
                    user_vornachname=vornachname,
                    user_email=email,
                    user_passwort=bcrypt.generate_password_hash(passwort).decode('utf-8'))
        
        db.session.add(user)
        db.session.commit()
        return user

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))