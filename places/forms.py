from django import forms
from .models import Place
# from django.contrib.gis import forms as gisForm


class PlaceForm(forms.ModelForm):

    class Meta:
        model = Place
        fields = ('title', 'description', 'type',
                  'address', 'phone', 'city', 'title', 'tags',)
