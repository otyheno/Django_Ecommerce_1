from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def productDetail(request, slug):
    #product = Product.objects.get(slug=slug)
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/product_detail.html', {'product': product})