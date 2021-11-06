from django.db.models import Count, fields
from django.forms.forms import Form
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView,TemplateView,ListView,DetailView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import RedirectView
from django.views.generic.edit import FormView
from .models import Team,User,TeamChat
from django.utils import timezone
from accounts.forms import TeamNewForm,TeamChatForm

class RegisterForm(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'
    
class Logout(LoginRequiredMixin,TemplateView):
    template_name = 'logout.html'

class TeamList(ListView):
    template_name = 'team_list.html'
    model = Team
    paginate_by = 20

class TeamDetail(DetailView):
    template_name = 'team_detail.html'
    model = Team

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        team = self.get_object()
        requested_user = self.request.user
        ctx['is_menber']=False
        for joined_user in team.menber.all():
            if joined_user == requested_user:
                ctx["is_menber"]=True
                break 
        return ctx

    def post(self, request, *args, **kwargs):
        join_user = request.user
        join_team = self.get_object()
        join_team.menber.add(join_user)
        join_team.save()
        return self.get(request, *args, **kwargs)
    
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

class TeamChat(CreateView, ListView):
    template_name = 'team_chat.html'
    model = TeamChat
    form_class = TeamChatForm
    paginate_by = 20
    # success_url = '/'  

    def get_success_url(self):
        success_url = self.request.path
        return success_url

    def form_valid(self, form):
        form.instance.menber_id = self.request.user.id
        form.instance.team_id = self.kwargs['teamid']
        return super(TeamChat,self).form_valid(form)

    def get_queryset(self, **kwargs):
        queryset = self.model.objects.filter(team=self.kwargs['teamid'])
        queryset.order_by('published_at')
        return queryset

    
            

   
    
# Create your views here.