from django.contrib import admin
from django.urls import path
from . import views


from .views import (
    CouponListCreateAPIView,
    CouponRetrieveUpdateDestroyAPIView
)



urlpatterns = [
    path('custom/master/view_coupons', views.load_view_coupons),
    path('custom/master/add_coupons', views.load_add_coupons),
    path('custom/master/delete_coupons/<int:cid>', views.delete_coupons),
    path('custom/master/edit_coupons/<int:cid>', views.edit_coupons),
    

    path('api/coupons/', CouponListCreateAPIView.as_view(), name='coupon-list-create'),
    path('api/coupons/<int:pk>/', CouponRetrieveUpdateDestroyAPIView.as_view(), name='coupon-rud'),
    
]