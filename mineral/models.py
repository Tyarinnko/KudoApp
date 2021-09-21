from django.db import models
from django.conf import settings
from django.utils import timezone
from taggit.managers import TaggableManager


class Mineral(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    tags = TaggableManager(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Create your models here.