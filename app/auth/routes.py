from flask import render_template, flash, request, redirect, url_for
from app.auth.forms import RegistrationForm
from app.auth import authentication as auth
from app.auth.models import User

@auth.route('/registrieren', methods=['GET', 'POST'])
def register_user():

    form = RegistrationForm()

    if form.validate_on_submit():
        User.create_user(
            user = form.name.data,
            email = form.email.data,
            passwort = form.passwort.data)
        flash('Anmeldung erfolgreich!')
        return redirect(url_for('main.display_home'))
    
    return render_template('registration.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login_user():
    return render_template('login.html')