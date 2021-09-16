from django import forms
from .models import Mineral

class MineralForm(forms.ModelForm):
    
    class Meta:
        model = Mineral
        fields = ("title","text")
    # TODO: write code...