from django.contrib import admin
from django.urls import path
from bakeryApp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.homepage,name='bakeryApp'),
    path("homepage",views.homepage,name='bakeryApp'),
    path("products",views.products,name='BakeryApp'),
    path("contactus",views.contactus,name='bakeryApp'),
    path("cart",views.cart,name='BakeryApp'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path("cart/",views.cart,name='cart'),

]
