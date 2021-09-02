from django.urls import path
from . import views

urlpatterns = [
    path('', views.MapList.as_view(), name='map_list'),
    path('map/<int:pk>/', views.MapDetail.as_view(), name='map_detail'),
    path('map/new/', views.MapNew.as_view(), name='map_new'),
    path('map/<int:pk>/edit/', views.MapEdit.as_view(), name='map_edit'),
    path('map/<int:pk>/delete/',views.MapDelete.as_view(),name='map_delete'),
    path('register',views.AccountRegistration.as_view(),name='registration')
]