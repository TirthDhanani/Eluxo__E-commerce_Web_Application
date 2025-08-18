from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('employees', views.load_employees),
    path('salaryslip', views.load_salaryslip)
]