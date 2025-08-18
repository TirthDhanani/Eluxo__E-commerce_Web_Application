from django.contrib import admin
from django.urls import path
from . import views 
urlpatterns = [
    path('order', views.placeOrder),
    path('order/myorders', views.viewMyOrders),
    path('order/items/<int:oid>', views.orderDetails),
    path('initiate_payment', views.initiate_payment),
    path('success/', views.payment_success, name='payment_success'),
    path('thank-you/', views.thank_you, name='thank_you'),
]