from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('custom/category/view', views.load_admin_categories),
    path('custom/category/add', views.load_add_category),
    path('custom/category/delete/<int:cid>', views.delete_category),
    path('custom/category/edit/<int:cid>', views.edit_category)
    ]
