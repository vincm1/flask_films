from flask import render_template, flash, request, redirect, url_for
from app.auth.forms import RegistrationForm
from app.auth import authentication as auth

@auth.route('/registrieren')
def register_user():
    form = RegistrationForm()
    return render_template('registration.html', form=form)