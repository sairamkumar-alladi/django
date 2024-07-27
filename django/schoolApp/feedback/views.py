from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def addFeedback(request):
    return render(request,'feedback/addfeedback.html')

def getFeedback(request):
    values = {"given_by":"sai","content":"All good but more attension is needed"}
    return render(request,'feedback/getfeedback.html',values)