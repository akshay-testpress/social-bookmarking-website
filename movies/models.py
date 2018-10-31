from django.db import models
# Create your models here.


class MoviesGenres(models.Model):
    title = models.CharField(max_length=100, null=False, unique=True)

    class Meta:
        verbose_name_plural = "MoviesGenres"

    def __str__(self):
        return str(self.title)


class MoviesDirectors(models.Model):
    GENDER_CHOICES = (
        (1, 'Male'),
        (2, 'Female'),
    )
    first_name = models.CharField(max_length=100)
    middel_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, null=True)
    ph_number = models.CharField(max_length=10, null=True, unique=True)
    birthdate = models.DateField(null=True)
    gender = models.SmallIntegerField(null=True, choices=GENDER_CHOICES)
    website = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name_plural = "MoviesDirectors"

    @property
    def display_gender(self):
        GENDER_CHOICES = dict(self.GENDER_CHOICES)
        return GENDER_CHOICES[self.gender]

    def __str__(self):
        return str(self.first_name) + ' ' + \
            str(self.middel_name) + ' ' + str(self.last_name)


class MoviesStudios(models.Model):
    title = models.CharField(max_length=100, unique=True)
    prefix = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name_plural = "MoviesStudios"

    def __str__(self):
        return self.title


class MoviesMaster(models.Model):
    title = models.CharField(max_length=100)
    prefix = models.CharField(max_length=100, null=True, blank=True)
    sub_title = models.CharField(max_length=100, blank=True)
    genre = models.ForeignKey(MoviesGenres, on_delete=models.PROTECT)
    directors = models.ManyToManyField(MoviesDirectors)
    studio = models.ForeignKey(MoviesStudios, on_delete=models.PROTECT)
    release_date = models.DateField()
    # will keep address of the field
    cover_image = models.CharField(
        max_length=100,
        blank=True
    )
    review = models.CharField(max_length=100)
    ASIN = models.CharField(max_length=100, blank=True)  # alpha numeric field

    def __str__(self):
        return str(self.genre)+' - '+str(self.title)

    @property
    def amazon_url(self):
        return "http://asin.info/a/"+str(self.ASIN)

    @property
    def get_all_directors_name(self):
        directors_queryset = MoviesMaster.objects.get(
            pk=self.id
        ).directors.all()
        return (', '.join(str(director) for director in directors_queryset))
