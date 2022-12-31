from django.shortcuts import render, get_object_or_404
from .models import Product, Category

# Create your views here.

def productDetail(request, slug, category_slug):
    #product = Product.objects.get(slug=slug)
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/product_detail.html', {'product': product})

def categoryDetail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'store/category_detail.html', {'category': category})