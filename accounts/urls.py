from django.urls import path
from .views import RegisterForm,Logout,TeamNew,TeamList,TeamEdit,TeamDetail

urlpatterns = [
    path('register/',RegisterForm.as_view(),name='register'),
    path('logout/',Logout.as_view(),name='logout'),
    path('team_list/',TeamList.as_view(),name='team_list'),
    path('team_new/',TeamNew.as_view(),name='team_new'),
    path('team_list/team_detail/<pk>/',TeamDetail.as_view(),name='team_detail'),    
    path('team_list/team_detail/<pk>/team_edit/',TeamEdit.as_view(),name='team_edit'),
    ]