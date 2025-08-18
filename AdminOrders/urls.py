from django.contrib import admin
from django.urls import path
from . import views 
urlpatterns = [
    path('custom/orders', views.load_orders),
    path('custom/orders/<int:oid>', views.load_order_details),
    path('custom/orderdetails/update_status', views.update_order_status)
]