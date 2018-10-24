from django.db import models
# Create your models here.



class MoviesGenres(models.Model):
    title = models.CharField(max_length=100,null=False,unique=True)

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
    middel_name = models.CharField(max_length=100,blank=True)
    last_name = models.CharField(max_length=100,null=True)
    ph_number = models.CharField(max_length=10,null=True,unique=True)
    birthdate = models.DateField(null=True)
    gender = models.SmallIntegerField(null=True,choices=GENDER_CHOICES)
    website = models.CharField(max_length=100,null=True,blank=True)

    class Meta:
        verbose_name_plural = "MoviesDirectors"

    @property
    def display_gender(self):
        GENDER_CHOICES = dict(self.GENDER_CHOICES)
        return GENDER_CHOICES[self.gender]

    def __str__(self):
        return str(self.first_name)+' '+str(self.middel_name)+' '+str(self.last_name)

class MoviesStudios(models.Model):
    title = models.CharField(max_length=100,unique=True)
    prefix = models.CharField(max_length=100,blank=True)
    website = models.CharField(max_length=100,blank=True)

    class Meta:
        verbose_name_plural = "MoviesStudios"

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in MoviesStudios._meta.fields]


    def __str__(self):
        return self.title

class MoviesMaster(models.Model):
    title = models.CharField(max_length=100)
    prefix = models.CharField(max_length=100,null=True,blank=True) 
    sub_title = models.CharField(max_length=100,blank=True)
    genre = models.ForeignKey(MoviesGenres,on_delete=models.CASCADE)
    directors = models.ForeignKey(MoviesDirectors,on_delete=models.CASCADE)
    studio = models.ForeignKey(MoviesStudios,on_delete=models.CASCADE)
    release_date = models.DateField()
    cover_image = models.CharField(max_length=100,blank=True)  #will keep address of the field
    review = models.CharField(max_length=100)
    ASIN = models.CharField(max_length=100,blank=True) #alpha numeric field


    def __str__(self):
        return str(self.genre)+' - '+str(self.title)
    
    def amazon_url(self):
        return str(self.ASIN)




    


