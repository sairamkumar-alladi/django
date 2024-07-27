from django.contrib import admin
from django.urls import path
from feedback import views

urlpatterns = [
    
    path('add/',views.addFeedback),
    path('get/',views.getFeedback),

]