from django.db import models
from django.contrib.gis.db.models import PointField
from taggit.managers import TaggableManager
import datetime
from socialWebsite.utils import get_unique_slug
from django.contrib.auth.models import User
# from taggit.models import Tag


class Country(models.Model):
    title = models.CharField(max_length=100, null=False)

    class Meta:
        verbose_name_plural = 'Country'

    def __str__(self):
        return str(self.title)


class City(models.Model):
    title = models.CharField(max_length=100, null=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'City'

    def __str__(self):
        return str(self.title)


class Type(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Type'

    def __str__(self):
        return str(self.title)


class Place(models.Model):
    title = models.CharField(max_length=250, null=False)
    location = PointField(null=True, blank=True)
    description = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=10, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    type = models.ManyToManyField(Type)
    tags = TaggableManager()
    slug = models.SlugField(unique=True)
    date_added = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Place'

    def __str__(self):
        return str(self.title)

    @property
    def get_all_tags(self):
        return ','.join(str(tag) for tag in Place.objects.get(
            pk=self.id
        ).tags.names())

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = get_unique_slug(self, Place)
            self.date_added = datetime.datetime.now()

        super(Place, self).save(*args, **kwargs)
