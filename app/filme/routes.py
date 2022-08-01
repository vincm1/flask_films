from app.filme import main
from app import db
from app.filme.forms import AddFilmForm
from app.filme.models import Film
from flask import render_template, flash, request, redirect, url_for


@main.route('/')
@main.route('/home')
def display_home():
    return render_template('home.html')

@main.route('/filme')
def display_filme():
    filme = Film.query.all()
    return render_template('alle_filme.html', filme=filme)

@main.route('/add/film', methods=["GET", "POST"])
def add_film():
    form = AddFilmForm()
    if form.validate_on_submit():
        film = Film(titel=form.titel.data, laenge=form.laenge.data, regie=form.regie.data, jahr=form.jahr.data, schauspieler=form.schauspieler.data, rating=form.rating.data, preise=form.preise.data, image = form.image.data)
        db.session.add(film)
        db.session.commit()
        flash("Success!")
    return render_template('add_film.html', form=form)

@main.route('/film/<film_id>', methods=["GET", "POST"])
def display_film(film_id):
    film = Film.query.get(film_id)
    return render_template('film_einzel.html', film=film, film_id = film.id)

@main.route('/edit/film/<film_id>', methods=["GET", "POST"])
def edit_film(film_id):
    film = Film.query.get(film_id)
    return render_template('film_einzel.html', film=film, film_id = film.id)