from django.contrib import admin
from .models import Film, GenreFilm, LinkFilm, CountryFilm, CollectionFilm, Collection, Country, Genre
# Register your models here.
admin.site.register(Film, GenreFilm, LinkFilm, CountryFilm, CollectionFilm, Collection, Country, Genre)

