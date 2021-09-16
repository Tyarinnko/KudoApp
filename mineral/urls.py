from django.urls import path
from . import views

urlpatterns = [
    path('mineral/',views.MineralList.as_view(),name='mineral_list'),
    path('mineral/<int:pk>/', views.MineralDetail.as_view(), name='mineral_detail'),
    ]