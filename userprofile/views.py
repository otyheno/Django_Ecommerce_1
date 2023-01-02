from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import UserProfile

from store.forms import ProductForm
from store.models import Product, Category

# Create your views here.

def vendorDetail(request, pk):
    user = User.objects.get(pk=pk)
    return render(request, 'userprofile/vendor_detail.html', {'user': user})

@login_required
def myStore(request):
    return render(request, 'userprofile/my_store.html')

@login_required
def addProduct(request):
    return render(request, 'userprofile/add_product.html')

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
            