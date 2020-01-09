from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Product

def index(request):
    text_var = 'This is my first Django app web page.'
    return HttpResponse(text_var)

#Category view

def allProdCat(request, c_slug=None):
    c_page = None
    products = None
    if c_slug =None:
        c+page = get_object_or_404(Category, slug=c_slug)
        products = Products.objects.filter(category=c_page, available=True)
    else:
        products = Prodcuts.objects.all().filter(available=True)
    return render(request, 'shop/category.html', {'category':c_page, 'products':products})