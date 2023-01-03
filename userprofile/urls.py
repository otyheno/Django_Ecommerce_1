from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    #path('product/', views.productDetail, name='product_detail'),
    path('signup/', views.signUp, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.myAccount, name='my_account'),
    path('my-store/', views.myStore, name='my_store'),
    path('my-store/add-product/', views.addProduct, name='add_product'),
    path('my-store/edit-product/<int:pk>/', views.editProduct, name='edit_product'),
    path('vendors/<int:pk>/', views.vendorDetail, name='vendor_detail'),
]