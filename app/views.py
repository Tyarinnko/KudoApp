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
from . forms import AccountForm,AddAccountForm
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse


class MapList(ListView):
    model = Map
    queryset = Map.objects.order_by('-created_date')

class MapDetail(DetailView):
    template_name = 'app/map_detail.html'
    model = Map

class MapNew(CreateView):
    template_name = 'app/map_edit.html'
    model = Map
    form_class = MapForm
    success_url = '/'

    def form_valid(self, form):
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
    
class AccountRegistration(TemplateView):
    def __init__(self):
        self.params = {
        "AccountCreate":False,
        "account_form":AccountForm(),
        "add_account_form":AddAccountForm(),
        }
        
    def get(self,request):
        self.params["account_form"] = AccountForm()
        self.params["add_account_form"] = AddAccountForm()
        self.params["AccountCreate"] = False
        return render(request,"app/register.html",context=self.params)
        
    def post(self,request):
        self.params["account_form"] = AccountForm(data=request.POST)
        self.params["add_account_form"] = AddAccountForm(data=request.POST)
        
        if self.params["account_form"].is_valid() and self.params["add_account_form"].is_valid():
            account = self.params["account_form"].save()
            account.set_password(account.password)
            account.save()
            add_account = self.params["add_account_form"].save(commit=False)
            add_account.user = account
            add_account.save()
            self.params["AccountCreate"] = True
        
        else:
            print(self.params["account_form"].errors)
            
        return render(request,"app/register.html",context=self.params)