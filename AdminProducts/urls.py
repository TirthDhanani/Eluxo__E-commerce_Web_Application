from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('api/getAllProducts', views.getAllProducts),
    path('api/create_product', views.create_product),
    path('custom/products/view', views.view_products),
    path('custom/products/add', views.add_products),
    path('custom/products/delete/<int:pid>', views.delete_products),
    path('custom/products/edit/<int:pid>', views.edit_products)
]