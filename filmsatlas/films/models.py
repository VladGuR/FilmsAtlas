from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(verbose_name='Жанры', max_length=100)
    desc = models.TextField(verbose_name='Описание', blank=True)
    img = models.ImageField(verbose_name='Картинка', blank=True, upload_to='ganre_img')
    seo_desc = models.TextField(verbose_name='Сео описание', blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Country(models.Model):
    name = models.CharField(verbose_name='Страна', max_length=150)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Collection(models.Model):
    name = models.CharField(verbose_name='Подборка', max_length=100)
    desc = models.TextField(verbose_name='Описание', blank=True)
    img = models.ImageField(verbose_name='Картинка', blank=True, upload_to='ganre_img')
    seo_desc = models.TextField(verbose_name='Сео описание', blank=True)
    sort = models.SmallIntegerField(verbose_name='Сортировка', default=0)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'


class Film(models.Model):
    name = models.CharField(verbose_name='Название фильма', unique=True, max_length=150)
    duration = models.CharField(verbose_name='Продолжительность', max_length=150, blank=True)
    year_of_release = models.DateField(verbose_name='Дата выпуска', default='1000-01-01', blank=True)
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
    film = models.ForeignKey(Film, verbose_name='Фильм', related_name='genre_film', to_field='name', on_delete=models.CASCADE)

    def json_dump_genre(self):
        return f'{self.genre.name}'


class CollectionFilm(models.Model):
    collection = models.ForeignKey(Collection, verbose_name='Подборка', related_name='collection', on_delete=models.CASCADE)
    film = models.ForeignKey(Film, verbose_name='Фильм', related_name='collection_film', on_delete=models.CASCADE)


