from django.contrib import admin
from .models import Category,Product
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)

# @admin.register(Category)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('id','name','email','password')