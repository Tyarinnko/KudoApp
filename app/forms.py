from django import forms
from .models import Map
from django.contrib.auth.models import User
from .models import Account


class MapForm(forms.ModelForm):

    class Meta:
        model = Map
        fields = ("place","hint",)
        
class AccountForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")
    
    class Meta:
        model = User
        fields = ('username','email','password')
        labels = {'username':"ユーザーID",'email':"メールアドレス"}
        
class AddAccountForm(forms.ModelForm):
    
    class Meta:
        model = Account
        fields = ('last_name','first_name',)
        labels = {'last_name':"苗字",'first_name':"名前",}