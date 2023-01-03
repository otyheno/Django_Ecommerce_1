from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.text import slugify
from .models import UserProfile

from store.forms import ProductForm
from store.models import Product

# Create your views here.

def vendorDetail(request, pk):
    user = User.objects.get(pk=pk)
    return render(request, 'userprofile/vendor_detail.html', {'user': user})

@login_required
def myStore(request):
    return render(request, 'userprofile/my_store.html')

@login_required
def addProduct(request):
    form = ProductForm
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            title = request.POST.get('title')
            product = form.save(commit=False)
            product.user = request.user
            product.slug = slugify(title)
            product.save()
            
            messages.success(request, "Product added successfully")
                        
            return redirect('my_store')
    else:
        form = ProductForm()
    return render(request, 'userprofile/add_product.html', {
        'title': 'Add Product',
        'form': form
        })

@login_required
def editProduct(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    #form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            
            messages.success(request, "Product saved successfully")
            
            return redirect('my_store')
    else:
        form = ProductForm(instance=product)
    return render(request, 'userprofile/add_product.html', {
        'title': 'Edit Product',
        'product': product,
        'form': form
        })
    
@login_required
def deleteProduct(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    product.status = Product.DELETED
    product.save()
    
    messages.success(request, "Product deleted successfully")
    
    return redirect('my_store')


def signUp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #username = form.cleaned_data.get('username')
            login(request, user)            
            userprofile = UserProfile.objects.create(user=user)
            return redirect('frontpage')
    else:
        form = UserCreationForm()
    
    return render(request, 'userprofile/signup.html', {'form': form})

@login_required
def myAccount(request):
    return render(request, 'userprofile/my_account.html')
            