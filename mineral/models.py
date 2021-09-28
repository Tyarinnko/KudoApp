from django.db import models
from django.conf import settings
from django.utils import timezone



class Mineral(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("鉱石名",max_length=200)
    text = models.TextField("説明文")
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Create your models here.