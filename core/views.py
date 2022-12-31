from django.shortcuts import render
from store.models import Product

# Create your views here.
def frontPage(request):
    products = Product.objects.all()[0:6]

    return render(request, 'core/frontpage.html', {'products': products})

def aboutPage(request):
    return render(request, 'core/aboutpage.html')
