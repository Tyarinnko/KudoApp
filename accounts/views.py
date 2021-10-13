from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView,TemplateView,ListView,DetailView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Team,User
from django.utils import timezone
from accounts.forms import TeamNewForm

class RegisterForm(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'
    
class Logout(LoginRequiredMixin,TemplateView):
    template_name = 'logout.html'

class TeamList(ListView):
    template_name = 'team_list.html'
    model = Team

class TeamDetail(DetailView):
    template_name = 'team_detail.html'
    model = Team

class TeamNew(CreateView):
    template_name = 'team_edit.html'
    model = Team 
    form_class = TeamNewForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.owner = User.objects.get(id=self.request.user.id)
        form.instance.published_date = timezone.now()
        return super(TeamNew,self).form_valid(form)

class TeamEdit(UpdateView):
    template_name = 'team_edit.html'
    model = Team
    form_class = TeamNewForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.owner = User.objects.get(id=self.request.user.id)
        form.instance.published_date = timezone.now()
        return super(TeamEdit,self).form_valid(form)
# Create your views here.