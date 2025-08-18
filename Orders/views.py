from django.shortcuts import render, redirect
from django.contrib import messages
from Cart.models import CartModel
from .models import OrderModel,Item
from django.http import JsonResponse
from AdminOrders.models import OrderlogModel
from AdminOrders.models import OrderlogModel
import razorpay
from django.conf import settings
import json

from django.views.decorators.csrf import csrf_exempt
def initiate_payment(request):
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    amount = float(request.POST.get("totalpayment"))
    # Amount in paisa: 500 Rs = 50000 paisa
    payment = client.order.create({
        'amount': amount * 100,
        'currency': 'INR',
        'payment_capture': '1'
    })


    state = request.POST.get('state')
    city = request.POST.get('city')
    addressline1 = request.POST.get('address_line1')
    addressline2 = request.POST.get('address_line2')
    pincode = request.POST.get('pincode')
    phone = request.POST.get('phone')


    context = {
        'key_id': settings.RAZORPAY_KEY_ID,
        'order_id': payment['id'],
        'amount': amount * 100,
        'state':state,
        'city':city,
        'addressline1':addressline1,
        'addressline2':addressline2,
        'pincode':pincode,
        'phone':phone,
    }
    return render(request, 'payment.html', context)

def thank_you(request):
    pk = request.session.get('order_id')
    orderdata = OrderModel.objects.get(user_id = request.user, order_id = pk)
    items = Item.objects.filter(order_id = pk)
    log = OrderlogModel()
    log.user_id = request.user
    log.order_id = OrderModel.objects.get(order_id = pk)
    log.status = orderdata.status
    log.save()
    if pk:
        del request.session['order_id']
    context = {
        'orderdata' : orderdata,
        'items' : items
    }
    return render(request, 'thank_you.html', context)

@csrf_exempt
def payment_success(request):
    data = json.loads(request.body)
    try:
        cartdata = CartModel.objects.filter(user = request.user)
        grandtotal = 0
        for row in cartdata:
            grandtotal += row.getproducttotal()
        state = data["state"]
        city =data["city"]
        addressline1 = data["addressline1"]
        addressline2 = data["addressline2"]
        pincode =data["pincode"]
        phone = data["phone"]
        if not phone.isdigit() and len(phone)!=10:
            messages.error(request, 'Please enter valid phone number!')
            return 
        obj = OrderModel()
        obj.user_id = request.user
        obj.total_payment = grandtotal
        obj.addressline1 = addressline1
        obj.addressline2 = addressline2
        obj.state = state
        obj.city = city
        obj.pincode = pincode
        #obj.transnumber = data["razorpay_payment_id"]
        obj.discount = request.session.get('disamt', 0)
        obj.contactnumber = phone 
        obj.save()


        #Log
        # log = OrderlogModel()
        # log.order_id = obj
        # log.status = 'pending'
        # log.save()



        request.session['order_id'] = obj.pk
        if 'disamt' in request.session:
            del request.session['disamt']

        cartdata = CartModel.objects.filter(user_id = request.user.id)
        for row in cartdata:
            iobj = Item()
            iobj.order_id = obj
            iobj.product_id = row.product_id
            iobj.quantity = row.quantity
            iobj.item_price = row.product_id.sell_price
            iobj.save()

            row.delete()

        return JsonResponse({'status': 'Payment Verified'})
    except Exception as e:
        return JsonResponse({'status': 'Verification Failed', 'error': str(e)})

   
def placeOrder(request):
    try:
        cartdata = CartModel.objects.filter(user = request.user)
        grandtotal = 0
        for row in cartdata:
            grandtotal += row.getproducttotal()
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        state = request.POST.get('state')
        city = request.POST.get('city')
        addressline1 = request.POST.get('address_line1')
        addressline2 = request.POST.get('address_line2')
        pincode = request.POST.get('pincode')
        phone = request.POST.get('phone')
        if not phone.isdigit() and len(phone)!=10:
            messages.error(request, 'Please enter valid phone number!')
            return 
        obj = OrderModel()
        obj.user_id = request.user
        obj.first_name = firstname
        obj.last_name = lastname
        obj.total_payment = grandtotal
        obj.addressline1 = addressline1
        obj.addressline2 = addressline2
        obj.state = state
        obj.city = city
        obj.pincode = pincode
        obj.discount = request.session.get('disamt', 0)
        obj.contactnumber = phone 
        obj.save()
       

        cartdata = CartModel.objects.filter(user_id = request.user.id)
        for row in cartdata:
            iobj = Item()
            iobj.order_id = obj
            iobj.product_id = row.product_id
            iobj.quantity = row.quantity
            iobj.item_price = row.product_id.sell_price
            iobj.save()

            row.delete()

        messages.success(request, 'Order placed successfully!')
    except Exception as e:
        messages.error(request, str(e))
    return redirect('/shop')

def viewMyOrders(request):
    orderdata = OrderModel.objects.filter(user_id = request.user)
    context = {
        'orderdata' : orderdata
    }
    return render(request, 'myorders.html', context)
def orderDetails(request,oid):
    orderdata = OrderModel.objects.get(user_id = request.user, order_id = oid)
    items = Item.objects.filter(order_id = oid)
    context = {
        'orderdata' : orderdata,
        'items' : items
    }
    return render(request, 'orderdetails.html', context)
