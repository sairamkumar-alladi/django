# myapp/forms.py
from django import forms
from .models import Category
class CategoryForm(forms.Form):
    name = forms.CharField(max_length=100)

class ProductForm(forms.Form):
    name = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    category = forms.ModelChoiceField(queryset=Category.objects.all())