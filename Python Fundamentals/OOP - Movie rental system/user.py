from movie import Movie


class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<User {}>".format(self.name)

    def add_movie(self, name, genre):
        movie = Movie(name, genre, False)
        self.movies.append(movie)

    def delete_movie(self, name):
        self.movies = list(filter(lambda movie: movie.name != name, self.movies))
        # import ipdb; ipdb.set_trace()

    def watched_movies(self):
        return list(filter(lambda movie: movie.watched, self.movies))

    def set_watched(self, name):
        for movie in self.movies:
            if name == movie.name:
                movie.watched = True

    def my_json(self):
        return {
            'name': self.name,
            'movies': [
                movie.json_repr() for movie in self.movies
            ]
        }

    @classmethod
    def from_json(cls, json_data):
        user = User(json_data['name'])
        movies = []
        for movie in json_data['movies']:
            movies.append(Movie.movie_converter(movie))
        user.movies = movies

        return user