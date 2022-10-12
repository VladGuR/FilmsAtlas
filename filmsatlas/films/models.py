from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(verbose_name='Жанры', unique=True, max_length=100)
    desc = models.TextField(verbose_name='Описание', blank=True)
    img = models.ImageField(verbose_name='Картинка', blank=True, upload_to='ganre_img')
    seo_desc = models.TextField(verbose_name='Сео описание', blank=True)

    def __str__(self):
        return f'{self.name}'

    def self_name(self):
        context = str(self.name)
        return context

    def check_genres(self):
        films = GenreFilm.objects.filter(genre_id=self.id)[:6]
        name = self.name[0].upper()+self.name[1:]
        context_films = [obj.film.check_film() for obj in films]
        context = {
            'name': name,
            'desc': self.desc,
            'films': context_films if context_films else "",
        }
        return context

    def json_dump_genre(self, quantity):
        if quantity:
            films = GenreFilm.objects.filter(genre_id=self.id)[:10]
        else:
            films = GenreFilm.objects.filter(genre_id=self.id)
        context_films = [obj.film.json_dump_film() for obj in films]
        context = {
            'genre': self.name,
            'films': context_films if context_films else "",
        }
        return context

    class Meta:
        ordering = ['name']
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Country(models.Model):
    name = models.CharField(verbose_name='Страна', unique=True, max_length=150)

    def __str__(self):
        return f'{self.name}'

    def self_name(self):
        context = str(self.name)
        return context

    def json_dump_country(self):
        films = CountryFilm.objects.filter(country=self.id)
        context_films = [obj.film.json_dump_film() for obj in films]
        context = {
            'country': self.name,
            'films': context_films if context_films else "",
        }
        return context

    class Meta:
        ordering = ['name']
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Collection(models.Model):
    name = models.CharField(verbose_name='Подборка', unique=True, max_length=100)
    desc = models.TextField(verbose_name='Описание', blank=True)
    img = models.ImageField(verbose_name='Картинка', blank=True, upload_to='ganre_img')
    seo_desc = models.TextField(verbose_name='Сео описание', blank=True)
    sort = models.SmallIntegerField(verbose_name='Сортировка', default=0)

    def __str__(self):
        return f'{self.name}'

    def check_filmcollection(self):
        collectionsfilm = CollectionFilm.objects.filter(collection_id=self.id)
        return collectionsfilm

    def json_dump_country(self, quantity):
        if quantity:
            films = CollectionFilm.objects.filter(collection_id=self.id)[:10]
        else:
            films = CollectionFilm.objects.filter(collection_id=self.id)
        context_films = [obj.film.json_dump_film() for obj in films]
        context ={
            'collection': self.name,
            'films': context_films if context_films else ""
        }
        return context

    class Meta:
        ordering = ['name']
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'


class Film(models.Model):
    name = models.CharField(verbose_name='Название фильма', max_length=150)
    duration = models.CharField(verbose_name='Продолжительность', max_length=150, blank=True)
    year_of_release = models.DateField(verbose_name='Дата выпуска', default='2000-01-01', blank=True)
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

    def __str__(self):
        return f'{self.name}'

    def check_film(self):
        genre = GenreFilm.objects.filter(film_id=self.id)
        country = CountryFilm.objects.filter(film_id=self.id)
        context_country = [obj.country.name for obj in country]
        context_genre = [obj.genre.name for obj in genre]
        context = {
            'name': self.name,
            'year_of_release': str(self.year_of_release),
            'duration': self.duration,
            'image': str(self.image.url if self.image else ""),
            'description': self.description if self.description else "",
            'genre': context_genre if context_genre else "",
            'country': context_country if context_country else "",
        }
        return context

    def check_collectionfilm(self):
        collectionsfilm = CollectionFilm.objects.filter(film_id=self.id)
        return collectionsfilm

    def check_country(self):
        country = CountryFilm.objects.filter(film_id=self.id)
        return country

    def check_ganre(self):
        genre = GenreFilm.objects.filter(film_id=self.id)
        return genre

    def check_linkfilm(self):
        linkfilm = LinkFilm.objects.filter(film_id=self.id)
        return linkfilm

    def json_dump_film(self):
        genre = GenreFilm.objects.filter(film_id=self.id)
        country = CountryFilm.objects.filter(film_id=self.id)
        context_country = [obj.json_dump_country() for obj in country]
        context_genre = [obj.json_dump_genre() for obj in genre]
        context={
            'name': self.name,
            'year_of_release': str(self.year_of_release),
            'duration': self.duration,
            'image': str(self.image.url if self.image else ""),
            'description': self.description if self.description else "",
            'genre': context_genre if context_genre else "",
            'context_country': context_country if context_country else "",
        }
        return context

    class Meta:
        ordering = ['year_of_release', 'saw', 'name', 'rating_imdb']
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class CountryFilm(models.Model):
    country = models.ForeignKey(Country, verbose_name='Страна', related_name='country', on_delete=models.CASCADE)
    film = models.ForeignKey(Film, verbose_name='Фильм', related_name='country_film', on_delete=models.CASCADE)

    def json_dump_country(self):
        return f'{self.country.name}'


class LinkFilm(models.Model):
    name = models.ForeignKey(Film, verbose_name='Фильм', related_name='link_film', on_delete=models.CASCADE)
    link_film = models.URLField(verbose_name='Ссылка на фильм', blank=True)


class GenreFilm(models.Model):
    genre = models.ForeignKey(Genre, verbose_name='Жанр', related_name='genre', on_delete=models.CASCADE)
    film = models.ForeignKey(Film, verbose_name='Фильм', related_name='genre_film', on_delete=models.CASCADE)

    def json_dump_genre(self):
        return f'{self.genre.name}'

    def json_dump_films(self):
        context = {
            'name': self.film.name,
            'image': str(self.film.image.url if self.film.image else ""),
            'year_of_release': str(self.film.year_of_release),
            'duration': self.film.duration,
        }
        return context


class CollectionFilm(models.Model):
    collection = models.ForeignKey(Collection, verbose_name='Подборка', related_name='collection', on_delete=models.CASCADE)
    film = models.ForeignKey(Film, verbose_name='Фильм', related_name='collection_film', on_delete=models.CASCADE)


