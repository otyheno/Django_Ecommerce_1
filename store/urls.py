from django.urls import path

from . import views

urlpatterns = [
    #path('product/', views.productDetail, name='product_detail'),
    path('search/', views.search, name='search'),
    path('add-to-cart/<int:product_id>/', views.addToCart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', views.removeFromCart, name='remove_from_cart'),
    path('cart/', views.cartView, name='cart'),
    path('<slug:slug>/', views.categoryDetail, name='category_detail'),
    path('<slug:category_slug>/<slug:slug>/', views.productDetail, name='product_detail'),
]