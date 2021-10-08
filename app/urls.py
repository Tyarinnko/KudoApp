from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.MapList.as_view(), name='map_list'),
    path('map/<int:pk>/', views.MapDetail.as_view(), name='map_detail'),
    path('map/new/', views.MapNew.as_view(), name='map_new'),
    path('map/<int:pk>/edit/', views.MapEdit.as_view(), name='map_edit'),
    path('map/<int:pk>/delete/',views.MapDelete.as_view(),name='map_delete'),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)