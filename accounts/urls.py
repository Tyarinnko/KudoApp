from django.urls import path
from .views import RegisterForm,Logout

urlpatterns = [
    path('register/',RegisterForm.as_view(),name='register'),
    path('logout/',Logout.as_view(),name='logout'),
]