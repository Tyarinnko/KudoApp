from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from .models import Team

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True,label="メールアドレス")
    nickname = forms.CharField(label="ニックネーム")
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")
    
    class Meta:
        model = User
        fields = ('username','email','nickname','password')

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class TeamNewForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = ('title','text')
