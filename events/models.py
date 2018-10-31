from django.db import models
from taggit.managers import TaggableManager
from places.models import Place
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel
from socialWebsite.utils import get_unique_slug


class Event(TimeStampedModel):
    title = models.CharField(max_length=100)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    description = models.CharField(max_length=250, null=True, blank=True)
    tags = TaggableManager()
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ["-created"]

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = get_unique_slug(self, Event)
        super(Event, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.title)

    @property
    def get_all_tags(self):
        return ','.join(str(tag) for tag in Event.objects.get(
            pk=self.id
        ).tags.names())


class EventTimes(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    is_all_day = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return str(self.event) + ' ' + str(self.start_time)
