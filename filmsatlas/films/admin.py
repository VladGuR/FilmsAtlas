from django.contrib import admin
from .models import Film, GenreFilm, LinkFilm, CountryFilm, CollectionFilm, Collection, Country, Genre
# Register your models here.
admin.site.register(Film)
admin.site.register(GenreFilm)
admin.site.register(LinkFilm)
admin.site.register(CountryFilm)
admin.site.register(CollectionFilm)
admin.site.register(Collection)
admin.site.register(Country)
admin.site.register(Genre)

