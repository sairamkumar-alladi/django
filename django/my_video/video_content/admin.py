from django.contrib import admin
from .models import Video
# Register your models here.

@admin.register(Video)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','title','video')