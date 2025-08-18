from django.shortcuts import render,redirect
from .models import CouponModel
from django.contrib import messages
from rest_framework import generics
from .serializers import CouponSerializer

class CouponListCreateAPIView(generics.ListCreateAPIView):
    queryset = CouponModel.objects.all()
    serializer_class = CouponSerializer

class CouponRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CouponModel.objects.all()
    serializer_class = CouponSerializer



# Create your views here.
def load_view_coupons(request):
    data = CouponModel.objects.all()
    context = {
        "coupondata": data
    }
    return render(request,'admin/coupon/view_coupon.html', context)
def load_add_coupons(request):
    if request.method == 'GET':
        return render(request,'admin/coupon/addcoupon.html')
    else: 
        try:
            couponcode = request.POST.get('code')
            mincartvalue = request.POST.get('min_value')
            maxcartvalue = request.POST.get('max_value')
            discount_percent = request.POST.get('discount')
            couponstatus = request.POST.get('status')
            obj = CouponModel()
            obj.coupon_code = couponcode
            obj.min_cart_value = mincartvalue
            obj.max_cart_value = maxcartvalue
            obj.discount_percent = discount_percent
            obj.coupon_stat = couponstatus
            obj.save()
            messages.success(request, "Coupon added!")
        except:
            messages.error(request, "Error")
        return redirect("/custom/master/view_coupons")
    
def delete_coupons(request,cid):
    try:
        obj= CouponModel.objects.get(coupon_id = cid)
        obj.delete()
        messages.success(request, "Coupon deleted Successfully!")
    except:
        messages.error(request, 'Error')
    return redirect("/custom/master/view_coupons")
def edit_coupons(request,cid):
    if request.method == "GET":
        coupondata = CouponModel.objects.get(coupon_id = cid)
        context = {
            'coupondata' : coupondata
        }
        return render(request, 'admin/coupon/edit_coupon.html', context)
    else:
        try:
            obj = CouponModel.objects.get(coupon_id = cid)
            couponcode = request.POST.get('code')
            mincartvalue = request.POST.get('min_value')
            maxcartvalue = request.POST.get('max_value')
            discount_percent = request.POST.get('discount')
            couponstatus = request.POST.get('status')
            obj.coupon_code = couponcode
            obj.min_cart_value = mincartvalue
            obj.max_cart_value = maxcartvalue
            obj.discount_percent = discount_percent
            obj.coupon_stat = couponstatus
            obj.save()
            messages.success(request, "Coupon edited successfully!")
        except Exception as e:
            messages.error(request, e)
        return redirect("/custom/master/view_coupons")
            

