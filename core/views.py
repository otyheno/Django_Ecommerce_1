from django.shortcuts import render

# Create your views here.
def frontPage(request):
    return render(request, 'core/frontpage.html')

def aboutPage(request):
    return render(request, 'core/aboutpage.html')
