import mineral
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from .models import Mineral
from app.models import Map
from mineral.forms import MineralForm
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import ContextMixin
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.utils import timezone

class MineralList(ListView):
    template_name = "mineral_list.html"
    model = Mineral
    paginate_by = 20
    
class MineralDetail(DetailView):
    template_name = "mineral_detail.html"
    model = Mineral
    paginate_by = 20
    
    def get_context_data(self, **kwargs):
        ctx =super().get_context_data(**kwargs)
        mineral = self.get_object()
        ctx['maps']=mineral.map_set.all()
        return ctx

class MineralNew(CreateView):
    model = Mineral
    form_class = MineralForm

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        form.instance.published_date = timezone.now()
        return super(MineralNew,self).form_valid(form)

# Create your views here.
