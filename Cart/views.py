from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CartModel
from AdminProducts.models import ProductModel
from AdminCoupons.models import CouponModel
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
# Create your views here.
def load_cart_page(request):
    cartdata = CartModel.objects.all()

    
    
    grandtotal = 0
    for row in cartdata:
        grandtotal  = grandtotal + float(row.getproducttotal())
    disamt = 0
    disamt = float(request.session.get('disamt', 0))
    grandtotal  = grandtotal - disamt
    context = {
        'cartdata' : cartdata,
        'grandtotal':grandtotal,
        'disamt':disamt
    }
    return render(request, 'cart.html', context)

def add_to_cart(request, pid=None):
    try:
        product = ProductModel.objects.get(product_id=pid)
        quantity = request.POST.get('quantity') or 1  
        
        chk = CartModel.objects.filter(product_id = pid,user = request.user).first()
        if chk is None:
            obj = CartModel()
            obj.product_id = product
            obj.user = User.objects.get(id = request.user.id)
            obj.quantity = int(quantity)
            obj.save()
        else:
            chk.quantity = int(chk.quantity) + int(quantity)
            chk.save()
        request.session.pop('disamt', None) 
        messages.success(request, "Product added to cart successfully!")
    except Exception as e:
        messages.error(request, "eRRor : " + str(e))

    return redirect('/cart')  
def delete_cart_item(request, cid):
    try:
        obj = CartModel.objects.get(cart_id = cid)
        request.session.pop('disamt', None) 
        obj.delete()
        messages.success(request, 'Item removed successfully from the cart')
    except Exception as e:
        messages.error(request, str(e))
    return redirect('/cart')
def update_cart(request):
    try:
        total_items = int(request.POST.get('total_items'))
        for i in range(1, total_items+1):
            cart_id = request.POST.get(f'cartid_{i}')
            quantity = request.POST.get(f'cartquantity_{i}')
            if cart_id and quantity:
                    obj = CartModel.objects.get(cart_id = cart_id, user_id = request.user)
                    obj.quantity = int(quantity)
                    obj.save()
                    request.session.pop('disamt', None) 
        messages.success(request, 'Cart updated successfully!')
    except Exception as e:
        messages.error(request, str(e))
            

    return redirect('/cart')



@csrf_exempt
def check_coupon(request):
    coupon_code = request.POST.get("coupon_code")
    total = request.POST.get("total")
    if CouponModel.objects.filter(coupon_code=coupon_code,coupon_stat='active').exists():
        obj = CouponModel.objects.filter(coupon_code=coupon_code,coupon_stat='active').first()
        if float(total) >= float(obj.min_cart_value) and float(total) <= float(obj.max_cart_value):
            disamt = float(total) * float(obj.discount_percent) / 100
            request.session['disamt'] = disamt
            return JsonResponse({"status":"found","disamt":disamt})
        else:
            return JsonResponse({"status":"notvalid","disamt":0})
    else:
        return JsonResponse({"status":"notfound","disamt":0})
def remove_discount(request):
    request.session.pop('disamt', None)  # pop won't throw error if key missing
    return redirect('/cart')








        

