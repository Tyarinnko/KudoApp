from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import Account

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nickname = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")
    
    
    class Meta:
        model = User
        fields = ('username','email','nickname','password')
        labels = {'username':"ユーザーID",'email':"メールアドレス",'nickname':"ニックネーム",}
        
