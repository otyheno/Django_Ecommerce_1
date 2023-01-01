from django.urls import path

from . import views

urlpatterns = [
    #path('product/', views.productDetail, name='product_detail'),
    path('vendors/<int:pk>/', views.vendorDetail, name='vendor_detail'),
]