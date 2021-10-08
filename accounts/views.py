from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Team
from django.utils import timezone
from accounts.forms import TeamEditForm

class RegisterForm(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'
    
class Logout(LoginRequiredMixin,TemplateView):
    template_name = 'logout.html'

class TeamEdit(CreateView):
    template_name = 'team_edit.html'
    model = Team 
    form_class = TeamEditForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        form.instance.published_date = timezone.now()
        return super(TeamEdit,self).form_valid(form)

    
# Create your views here.