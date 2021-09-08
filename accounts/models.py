from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    nickname = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user.username
# Create your models here.
