from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Genre, Movie

app = Flask(__name__)

engine = create_engine('sqlite:///genremovie.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()



@app.route('/genre/<int:genre_id>/movie/JSON')
def genreMovieJSON(genre_id):
    genre = session.query(Genre).filter_by(id=genre_id).one()
    movies = session.query(Movie).filter_by(
        genre_id=genre_id).all()
    return jsonify(Movie=[i.serialize for i in movies])


@app.route('/genre/<int:genre_id>/movie/<int:movie_id>/JSON')
def movieJSON(genre_id, movie_id):
    Movie_detail = session.query(Movie).filter_by(id=movie_id).one()
    return jsonify(Movie_detail=Movie_detail.serialize)


@app.route('/genre/JSON')
def genresJSON():
    genres = session.query(Genre).all()
    return jsonify(genres=[r.serialize for r in genres])



# Show all genres
@app.route('/')
@app.route('/genre/')
def showGenres():
    genres = session.query(Genre).all()
    #return "This page will show all genres"
    return render_template('genre.html', genres=genres)


# Create a new genre
@app.route('/genre/new/', methods=['GET', 'POST'])
def newGenre():
    if request.method == 'POST':
        newGenre = Genre(name=request.form['name'])
        session.add(newGenre)
        session.commit()
        return redirect(url_for('showGenres'))
    else:
        return render_template('newGenre.html')
        #return "This page will be for making a new genre"

# Edit a genre


@app.route('/genre/<int:genre_id>/edit/', methods=['GET', 'POST'])
def editGenre(genre_id):
    editedGenre = session.query(
        Genre).filter_by(id=genre_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedGenre.name = request.form['name']
            return redirect(url_for('showGenres'))
    else:
        return render_template(
            'editGenre.html', genre=editedGenre)

        #return 'This page will be for editing genre %s' % genre_id

# Delete a genre


@app.route('/genre/<int:genre_id>/delete/', methods=['GET', 'POST'])
def deleteGenre(genre_id):
    genreToDelete = session.query(
        Genre).filter_by(id=genre_id).one()
    if request.method == 'POST':
        session.delete(genreToDelete)
        session.commit()
        return redirect(
            url_for('showGenres', genre_id=genre_id))
    else:
        return render_template(
            'deleteGenre.html', genre=genreToDelete)
        #return 'This page will be for deleting genre %s' % genre_id


# Show movies in a genre
@app.route('/genre/<int:genre_id>/')
@app.route('/genre/<int:genre_id>/movie/')
def showMovie(genre_id):
    genre = session.query(Genre).filter_by(id=genre_id).one()
    movies = session.query(Movie).filter_by(
        genre_id=genre_id).all()
    return render_template('movie.html', movies=movies, genre=genre)
    #return 'This page is the movie list for genre %s' % genre_id

# Create a new movie


@app.route(
    '/genre/<int:genre_id>/movie/new/', methods=['GET', 'POST'])
def newMovie(genre_id):
    if request.method == 'POST':
        newMovie = Movie(name=request.form['name'], description=request.form[
                           'description'], director=request.form['director'], starring=request.form['starring'], genre_id=genre_id)
        session.add(newMovie)
        session.commit()
        flash("new movie created!")
        return redirect(url_for('showMovie', genre_id=genre_id))
    else:
        return render_template('newmovie.html', genre_id=genre_id)

   
        #return 'This page is for listing a new movie for genre %s' %genre_id

# Edit a movie


@app.route('/genre/<int:genre_id>/movie/<int:movie_id>/edit',
           methods=['GET', 'POST'])
def editMovie(genre_id, movie_id):
    editedMovie = session.query(Movie).filter_by(id=movie_id).one()
     
    if request.method == 'POST':
        if request.form['name']:
            editedMovie.name = request.form['name']
        if request.form['description']:
            editedMovie.description = request.form['description']
        if request.form['director']:
            editedMovie.director = request.form['director']
        if request.form['starring']:
            editedMovie.course = request.form['starring']
        session.add(editedMovie)
        session.commit()
        flash('Movie Successfully Edited')
        return redirect(url_for('showMovie', genre_id=genre_id))
    else:
        
        return render_template(
            'editmovie.html', genre_id=genre_id, movie_id=movie_id, movie=editedMovie)

        #return 'This page is for editing movie %s' % movie_id

# Delete a movie


@app.route('/genre/<int:genre_id>/movie/<int:movie_id>/delete',
           methods=['GET', 'POST'])
def deleteMovie(genre_id, movie_id):
    movieToDelete = session.query(Movie).filter_by(id=movie_id).one()
    if request.method == 'POST':
        session.delete(movieToDelete)
        session.commit()
        return redirect(url_for('showMovie', genre_id=genre_id))
    else:
        return render_template('deleteMovie.html', movie=movieToDelete)
        #return "This page is for deleting movie %s" % movie_id


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000, threaded=False)