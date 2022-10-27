from django_unicorn.components import UnicornView, QuerySetType
from movies.models import Movie


class MovielistView(UnicornView):
    name: str = ""
    movies: QuerySetType[Movie] = Movie.objects.none()

    def mount(self):
        self.movies = Movie.objects.all()

    def add_movie(self):
        Movie.objects.create(name=self.name)
        self.name = ""
        self.movies = Movie.objects.all()

    def delete_all(self):
        Movie.objects.all().delete()
        self.movies = Movie.objects.none()
