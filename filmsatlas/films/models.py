from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(verbose_name='Жанры', max_length=100)
    desc = models.TextField(verbose_name='Описание', blank=True)
    img = models.ImageField(verbose_name='Картинка', blank=True, upload_to='ganre_img')
    seo_desc = models.TextField(verbose_name='Сео описание', blank=True)


class Country(models.Model):
    name = models.CharField(verbose_name='Страна', max_length=150)


class Collection(models.Model):
    name = models.CharField(verbose_name='Подборка', max_length=100)
    desc = models.TextField(verbose_name='Описание', blank=True)
    img = models.ImageField(verbose_name='Картинка', blank=True, upload_to='ganre_img')
    seo_desc = models.TextField(verbose_name='Сео описание', blank=True)
    sort = models.SmallIntegerField(verbose_name='Сортировка', default=0)


class Film(models.Model):
    name = models.CharField(verbose_name='Название фильма', max_length=150)
    duration = models.CharField(verbose_name='Продолжительность', max_length=150, blank=True)
    year_of_release = models.DateField(verbose_name='Дата выпуска', blank=True)
    age = models.SmallIntegerField(verbose_name='Возраст', default=0, blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    image = models.ImageField(verbose_name='Картинка', upload_to='film_img', blank=True)
    link_trailer = models.URLField(verbose_name='Ссылка на трейлер', blank=True)
    rating_kp = models.CharField(verbose_name='Рейтинг кп', max_length=10, blank=True)
    rating_imdb = models.CharField(verbose_name='Рейтинг imdb', max_length=10, blank=True)
    date_add = models.DateTimeField(verbose_name='Дата добавления', auto_now_add=True)
    seo_desc = models.TextField(verbose_name='Сео описание', blank=True)
    saw = models.IntegerField(verbose_name='Просмотры', default=0, blank=True)
    rating_fa = models.IntegerField(verbose_name='Рейтинг fa', default=0, blank=True)


class CountryFilm(models.Model):
    country = models.ForeignKey(Country, verbose_name='Страна', related_name='country', on_delete=models.CASCADE)
    film = models.ForeignKey(Film, verbose_name='Фильм', related_name='country_film', on_delete=models.CASCADE)


class LinkFilm(models.Model):
    name = models.ForeignKey(Film, verbose_name='Фильм', related_name='link_film', on_delete=models.CASCADE)
    link_film = models.URLField(verbose_name='Ссылка на фильм', blank=True)


class GenreFilm(models.Model):
    genre = models.ForeignKey(Genre, verbose_name='Жанр', related_name='genre', on_delete=models.CASCADE)
    film = models.ForeignKey(Film, verbose_name='Фильм', related_name='genre_film', on_delete=models.CASCADE)


class CollectionFilm(models.Model):
    collection = models.ForeignKey(Collection, verbose_name='Подборка', related_name='collection', on_delete=models.CASCADE)
    film = models.ForeignKey(Film, verbose_name='Фильм', related_name='collection_film', on_delete=models.CASCADE)


