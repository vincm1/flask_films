from app import create_app, db
from app.auth.models import User

if __name__ == '__main__':
    flask_app = create_app('dev')
    with flask_app.app_context():
        db.create_all()
        if not User.query.filter_by(user_name="MaxMuster").first():
            User.create_user(user="MaxMuster", email="MaxMuster@gmail.com", passwort='secret')
    flask_app.run()

