from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('students', views.load_result),
    path('result', views.add_avg)
   
]