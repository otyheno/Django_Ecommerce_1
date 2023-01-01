from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core.views import frontPage, aboutPage

urlpatterns = [
    path('about/', aboutPage, name='aboutpage'),
    path('admin/', admin.site.urls),
    path('', include('userprofile.urls')), 
    path('', include('store.urls')),
    path('', frontPage, name='frontpage'),     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
