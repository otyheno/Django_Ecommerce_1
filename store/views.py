from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from .cart import Cart

# Create your views here.
def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(status=Product.ACTIVE).filter(Q(title__icontains=query) | Q(description__icontains=query))
    
    return render(request, 'store/search.html', {
        'query': query,
        'products': products,
        })
    
def categoryDetail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(status=Product.ACTIVE)
    return render(request, 'store/category_detail.html', {
        'category': category,
        'products': products
        })

def productDetail(request, category_slug, slug):
    #product = Product.objects.get(slug=slug)
    #cart = Cart(request)
    #print(cart.getTotalCost())
    product = get_object_or_404(Product, slug=slug, status=Product.ACTIVE)
    return render(request, 'store/product_detail.html', {'product': product})

def addToCart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return redirect('cart')

def removeFromCart(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)
    return redirect('cart')


def cartView(request):
    cart = Cart(request)
    return render(request,'store/cart_view.html', {'cart': cart})