from app.filme import main
from app import db
from app.filme.forms import AddFilmForm, EditFilmForm
from app.filme.models import Film
from flask import render_template, flash, request, redirect, url_for
from flask_login import login_required

@main.route('/')
@main.route('/home')
def display_home():
    return render_template('home.html')

@main.route('/filme')
@login_required
def display_filme():
    filme = Film.query.all()
    return render_template('alle_filme.html', filme=filme)

@main.route('/add/film', methods=["GET", "POST"])
@login_required
def add_film():
    form = AddFilmForm()
    if form.validate_on_submit():
        film = Film(titel=form.titel.data, laenge=form.laenge.data, regie=form.regie.data, jahr=form.jahr.data, schauspieler=form.schauspieler.data, rating=form.rating.data, preise=form.preise.data, image = form.image.data)
        db.session.add(film)
        db.session.commit()
        flash("Success!")
        return redirect (url_for('main.display_filme'))
    return render_template('add_film.html', form=form)

@main.route('/film/<film_id>', methods=["GET", "POST"])
@login_required
def display_film(film_id):
    film = Film.query.get(film_id)
    return render_template('film_einzel.html', film=film, film_id=film.id)

@main.route('/edit/film/<film_id>', methods=["GET", "POST"])
@login_required
def edit_film(film_id):
    film = Film.query.get(film_id)
    form = EditFilmForm(obj=film)
    if form.validate_on_submit():
        film.titel = form.titel.data
        film.laenge = form.laenge.data
        film.regie = form.regie.data
        film.jahr = form.jahr.data
        film.image = form.image.data
        film.schauspieler = form.schauspieler.data
        film.rating = form.rating.data
        film.preise = form.preise.data

        db.session.add(film)
        db.session.commit()
        flash("Film bearbeitet!")
        return redirect(url_for('main.display_filme'))
    return render_template('edit_film.html', film=film, film_id = film.id, form=form)

@main.route('/delete/film/<film_id>', methods=["GET", "POST"])
@login_required
def delete_film(film_id):
    film = Film.query.get(film_id)
    if request.method == "POST":
        db.session.delete(film)
        db.session.commit()
        flash("Film gelöscht!")
        return redirect(url_for('main.display_filme'))
    return render_template('delete_film.html', film=film, film_id=film.id)

