from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.load_home),
    path('about', views.load_about),
    path('register', views.load_register),
    path('checklogin', views.checklogin),
    path('checklogout', views.checklogout),
    path('checkout', views.checkout),
    path('forgotpassword', views.load_forgot_password),
    path('otp', views.otpverify),
    path('setnewpass', views.setnewpass)
]
