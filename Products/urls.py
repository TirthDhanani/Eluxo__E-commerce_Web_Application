from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('view/<int:pid>', views.load_viewproduct),
    path('shop', views.load_menuproduct),
    path('shopajax', views.load_ajax_product),
    path('load_products', views.load_products),
    path('shop/<int:cid>', views.load_menuproduct),
    path('product/shop/review', views.add_review),
]