from django.shortcuts import render, redirect
from Orders.models import OrderModel, Item
from AdminOrders.models import OrderlogModel
from django.contrib import messages
# Create your views here.
def load_orders(request):
    orderdata = OrderModel.objects.all()
    context ={
        'orderdata' : orderdata
    }
    return render(request, 'admin/orders/orderlist.html', context)

def load_order_details(request,oid):
    orderdata = OrderModel.objects.get(order_id=oid)
    itemdata = Item.objects.filter(order_id=oid)
    context ={
        'orderdata' : orderdata,
        'itemdata' :itemdata   
    }
    return render(request, 'admin/orders/orderdetails.html', context)
def update_order_status(request):
    try: 
        orderid = request.POST.get('order_id')
        status = request.POST.get('status')
        obj = OrderModel.objects.get(order_id = orderid)
        obj.status = status
        obj.save()

        log = OrderlogModel()
        log.order_id = OrderModel.objects.get(order_id = orderid)
        log.status = status
        log.save()
        messages.success(request, 'Order status updated successfully!')

    except Exception as e:
        messages.error(request, str(e))
    return redirect(f'/custom/orders/{orderid}')

    
   





