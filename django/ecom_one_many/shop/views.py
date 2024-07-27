from django.shortcuts import render,redirect
from .models import Category,Product
# Create your views here.
from .forms import CategoryForm, ProductForm

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            # Process the form data as needed
            category_name = form.cleaned_data['name']
            # Perform actions with the data, such as creating a Category instance in the database
            # Example: Category.objects.create(name=category_name)
            cat = Category(name=category_name)
            cat.save()   
            return redirect('/')
    else:
        form = CategoryForm()

    return render(request, 'create_category.html', {'form': form})


def create_product(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            # Process the form data as needed
            product_data = form.cleaned_data
            # Perform actions with the data, such as creating a Product instance in the database
            # Example: Product.objects.create(**product_data)
            Product.objects.create(**product_data)
            return redirect('/')
    else:
        form = ProductForm()

    return render(request, 'create_product.html', {'form': form,'categories':categories})

def index(request):
    categories = Category.objects.all()
    return render(request,'index.html',context={'categories':categories})

def get_products(request,name):
    products = Product.objects.filter(category__name=name)
    return render(request,'products.html',context={'products':products,'category':name})