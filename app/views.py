import app
from typing import KeysView
from django import db, forms
from django.core.files.base import ContentFile
from django.db import models
from django.http import request
from django.urls.base import reverse_lazy
from django.views.generic.base import ContextMixin
from django.views.generic.edit import DeleteView
from app.forms import MapForm
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .models import Map
from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,TemplateView
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse


class MapList(ListView):
    model = Map
    queryset = Map.objects.order_by('-created_date')
    pagenate_by = 3

class MapDetail(DetailView):
    template_name = 'app/map_detail.html'
    model = Map

class MapNew(CreateView):
    template_name = 'app/map_edit.html'
    model = Map
    form_class = MapForm
    success_url = '/'

    def post(self, request, *arg,**kwargs):
        print(self.request.POST.items())
        return super().post(request, *arg,**kwargs)
    def form_valid(self, form):
        print(self.request)
        form.instance.author_id = self.request.user.id
        form.instance.published_date = timezone.now()
        return super(MapNew,self).form_valid(form)

class MapEdit(UpdateView):
    template_name = 'app/map_edit.html'
    model = Map
    form_class = MapForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        form.instance.published_date = timezone.now()
        return super(MapEdit,self).form_valid(form)

class MapDelete(DeleteView):
    template_name = 'app/map_delete.html'
    model = Map
    form_class = MapForm
    success_url = '/'
    