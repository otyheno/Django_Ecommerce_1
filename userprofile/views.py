from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.

def vendorDetail(request, pk):
    user = User.objects.get(pk=pk)
    return render(request, 'userprofile/vendor_detail.html', {'user': user})

