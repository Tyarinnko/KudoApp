from django.urls import path
from .views import RegisterForm,Logout,TeamEdit

urlpatterns = [
    path('register/',RegisterForm.as_view(),name='register'),
    path('logout/',Logout.as_view(),name='logout'),
    path('team_edit/',TeamEdit.as_view(),name='team_edit'),
    ]