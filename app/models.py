from django.conf import settings
from django.db import models
from django.contrib.auth.models import update_last_login
from django.utils import timezone

class Map(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    place = models.CharField("場所",max_length=200)
    hint = models.TextField("ヒント")
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.place
        
        
# Create your models here.
