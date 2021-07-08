from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name = 'home'),

    # product urls
    path('product/', views.product, name='product'),
    path('add_new_product/', views.addproduct, name = 'addproduct'),
    path('edit_product/<str:pk>/',views.editproduct, name= 'editproduct'),
    path('delete_product/<str:pk>/',views.deleteproduct, name= 'deleteproduct'),

    # customer urls
    path('customer/', views.customer, name = 'customer'),
    path('add_new_customer/', views.addcustomer, name = 'addcustomer'),
    path('edit_customer/<str:pk>/',views.editcustomer, name= 'editcustomer'),
    path('delete_customer/<str:pk>/',views.deletecustomer, name= 'deletecustomer'),
]