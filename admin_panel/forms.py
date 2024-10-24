from django import forms
from products.models import Product 
from categories.models import Category 

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'unit_sold', 'in_stock', 'expire_date','image' , 'category']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name','image']