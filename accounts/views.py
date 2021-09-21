from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class RegisterForm(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'
    
class Logout(LoginRequiredMixin,TemplateView):
    template_name = 'logout.html'
    
# Create your views here.