from django.contrib import admin
from django.urls import path
from .  import views 
urlpatterns = [
    path('custom/subcategory/view', views.admin_subcategory),
    path('custom/subcategory/add', views.add_subcategory),
    path('custom/subcategory/delete/<int:sid>', views.delete_subcategory),
    path('custom/subcategory/edit/<int:sid>', views.edit_subcategory)
]