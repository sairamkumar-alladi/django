from django.contrib import admin

# Register your models here.
from django.contrib import admin
from signal_app.models import Profile

admin.site.register(Profile)