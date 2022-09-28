import django.forms as forms
from .models import Film, GenreFilm, LinkFilm, CountryFilm, CollectionFilm, Genre, Collection, Country


class CreateGenre(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

