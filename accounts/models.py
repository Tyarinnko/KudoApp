from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100)
    
    def __str__(self):
        return self.user.username

class Team(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='team_owner')
    title = models.CharField("チーム名",max_length=100)
    text = models.TextField("紹介文")

    def __str__(self):
        return '<' + self.title + '(' + str(self.owner) + '>'

class Friends(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='friend_owner')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    team = models.ForeignKey(Team,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + '(team:"' + str(self.group) + '")'
    
# Create your models here.
