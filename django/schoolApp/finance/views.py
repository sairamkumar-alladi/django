from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def feeCollection(request):
    return HttpResponse('<h1>This is fee collection view</h1>')
def feeDueReport(request):
    return HttpResponse('<h1>This is fee Due Report view</h1>')
def feePaidReport(request):
    return HttpResponse('<h1>This is fee Paid Report view</h1>')