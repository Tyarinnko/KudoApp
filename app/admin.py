from django.contrib import admin
from .models import Map

admin.site.register(Map)

class AppAdmin(admin.ModelAdmin):
    list_display = ('id','place','tag_list')
    list_display_links = ('id','place')
    
    def get_queryset(self,request):
        return super().get_queryset(request).prefetch_related('tags')
        
    def tag_list(self,obj):
        return u",".join(o.name for o in obj.tags.all())
# Register your models here.
