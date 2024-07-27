from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentAdmissionModel

# Create your views here.

def addAdmission(request):
    return HttpResponse("This is add admission view")

def admissionReport(request):
    result = StudentAdmissionModel.objects.all()
    students = {'alldet':result}
    return render(request,'admission/admissionreport.html',students)



