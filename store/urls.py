from django.urls import path

from . import views

urlpatterns = [
    #path('product/', views.productDetail, name='product_detail'),
    path('<slug:slug>/', views.categoryDetail, name='category_detail'),
    path('<slug:category_slug>/<slug:slug>/', views.productDetail, name='product_detail'),
    
]