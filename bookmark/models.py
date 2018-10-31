from django.db import models


class LinkMaster(models.Models):
    user = models.ForeignKey(on_delete=models.CASCADE)
    link = models.CharField(max_length=500, null=False)
    name = models.CharField(max_length=250, null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    slug = models.SlugField(unique=True)
    is_deleted = models.BooleanField(default=False)

    def __self__(self):
        return str(self.name)
