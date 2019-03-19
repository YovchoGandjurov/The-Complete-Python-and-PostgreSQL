class Movie:
    def __init__(self, name, genre, watched):
        self.name = name
        self.genre = genre
        self.director = "Wachowski"
        self.watched = watched

    def __repr__(self):
        return "<Movie {}>".format(self.name)

    def json_repr(self):
        return {
            'name': self.name,
            'genre': self.genre,
            'watched': self.watched
        }

    @classmethod
    def movie_converter(cls, json_data):
        # return Movie(name=data['name'], genre=data['genre'], watched=data['watched'])
        return Movie(**json_data)        # the same as above
