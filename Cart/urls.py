from django.contrib import admin
from django.urls import path
from . import views 
urlpatterns = [
    path('cart/add/<int:pid>' , views.add_to_cart),
    path('cart', views.load_cart_page),
    path('cart/delete/<int:cid>', views.delete_cart_item),
    path('cart/update', views.update_cart),
    path('check_coupon', views.check_coupon),
    path('remove_discount', views.remove_discount)
]