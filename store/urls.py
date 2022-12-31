from django.urls import path

from . import views

urlpatterns = [
    #path('product/', views.productDetail, name='product_detail'),
    path('<slug:slug>/', views.productDetail, name='product_detail'),
]