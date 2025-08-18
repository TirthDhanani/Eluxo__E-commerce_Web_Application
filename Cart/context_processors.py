from .models import CartModel
from django.shortcuts import render, redirect

def cart_preview(request):
    cartdata = CartModel.objects.all()
    subtotal = 0
    total_items = 0
    for row in cartdata:
        subtotal += float(row.getproducttotal())
        total_items += row.quantity 

    return {
        'cartdata': cartdata,
        'subtotal': subtotal,
        'total_items': total_items
    }