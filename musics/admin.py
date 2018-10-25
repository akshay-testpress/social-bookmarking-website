from django.contrib import admin
from . import models 
# Register your models here.

admin.site.register(models.MusicGenres)
admin.site.register(models.CoverImages)
admin.site.register(models.LabelMaster)
admin.site.register(models.Musics)
admin.site.register(models.Albums)
admin.site.register(models.Artists)
admin.site.register(models.Bands)
admin.site.register(models.ArtistInAlbums)
admin.site.register(models.ArtistInMusics)
