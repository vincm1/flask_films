from flask import render_template, flash, request, redirect, url_for
from app.auth.forms import RegistrationForm, LoginForm
from app.auth import authentication as auth
from app.auth.models import User
from flask_login import login_user, logout_user, login_required, current_user

@auth.route('/registrieren', methods=['GET', 'POST'])
def register_user():

    form = RegistrationForm()

    if form.validate_on_submit():
        User.create_user(
            user = form.name.data,
            vornachname= form.vornachname.data,
            email = form.email.data,
            passwort = form.passwort.data)
        flash('Anmeldung erfolgreich!')
        return redirect(url_for('authentication.do_login_user'))
    
    return render_template('registration.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def do_login_user():

    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(user_email=form.email.data).first()
        if not user or not user.check_passwort(form.passwort.data):
            flash('Falsche Anmeldedaten!')
            redirect(url_for('authentication.do_login_user'))
        
        login_user(user, remember=True)
        return redirect(url_for('main.display_filme'))

    return render_template('login.html', form=form)

@auth.route('/logout')
@login_required
def do_logout_user():
    logout_user()
    return redirect(url_for('main.display_home'))

@auth.app_errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404