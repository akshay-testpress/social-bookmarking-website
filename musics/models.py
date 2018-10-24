from django.db import models

class CoverImages():
    image_name = models.CharField(max_length=50)
    image_location = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "CoverImages"

    def __str__(self):
        return self.image_name

class MusicGeners():
    title = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = "MusicGeners"

    def __str__(self):
        return self.title

class Bands():
    title = models.CharField(max_length=100)
    prefix = models.CharField(max_length=100, blank=True)
    slogan = models.CharField(max_length=100, blank=True)
    date_formed = models.DateField()

    class Meta:
        verbose_name_plural = "Bands"

    def __str__(self):
        return self.title +' '+ self.date_formed

class LabelMaster():
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, blank=True)
    est_date = models.DateField()

    class Meta:
        verbose_name_plural = "LabelMaster"

    def __str__(self):
        return self.title +' '+ self.subtitle

class Artists():
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    band_id = models.ForeignKey(Bands,on_delete=models.PROTECT, blank=True, null=True)
    label_id = models.ForeignKey(LabelMaster,on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Artists"

    def __str__(self):
        return self.first_name+' '+self.middle_name+' '+self.last_name

class Albums():
    title = models.CharField(max_length=50)
    prefix = models.CharField(max_length=50, blank=True) 
    subtitle = models.CharField(max_length=50, blank=True)
    total_track = models.SmallIntegerField(blank=True)
    release_date = models.DateField()
    cover_image_id = models.ForeignKey(CoverImages,on_delete=models.PROTECT, blank=True, null=True)
    gener_id = models.ForeignKey(MusicGeners,on_delete=models.PROTECT, blank=True, null=True)
    band_id = models.ForeignKey(Bands,on_delete=models.PROTECT, blank=True, null=True)
    label_id = models.ForeignKey(LabelMaster,on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Albums"

    def __str__(self):
        return self.prefix+' '+self.title

class Musics():
    title = models.CharField(max_length=50)
    track_number = models.SmallIntegerField(blank=True)
    length = models.TimeField()
    release_date = models.DateField()
    band_id = models.ForeignKey(Bands,on_delete=models.PROTECT, blank=True, null=True)
    label_id = models.ForeignKey(LabelMaster,on_delete=models.PROTECT, blank=True, null=True)
    album_id = models.ForeignKey(Albums,on_delete=models.PROTECT, blank=True, null=True)
    cover_image_id = models.ForeignKey(CoverImages,on_delete=models.PROTECT, blank=True, null=True)
    gener_id = models.ForeignKey(MusicGeners,on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Musics"

    def __str__(self):
        return self.title

class ArtistInMusics():
    music_id = models.ForeignKey(Musics,on_delete=models.CASCADE) 
    artist_id = models.ForeignKey(Artists,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "ArtistInMusics"

class ArtistInAlbums():
    album_id = models.ForeignKey(Albums,on_delete=models.CASCADE) 
    artist_id = models.ForeignKey(Artists,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "ArtistInAlbums" 



