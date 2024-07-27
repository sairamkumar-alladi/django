from django.shortcuts import render
from .models import Category,Product
# Create your views here.


def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    print(categories)
    context = {
        'categories':categories,
        'products' : products
    }
    return render(request,'index.html',context=context)

def category(request,name):
    categories = Category.objects.get(name=name)

    products = Product.objects.filter(category=categories)
    context = {
        'categories':categories,
        'products' : products
    }
    return render(request,'categories.html',context=context)