from django.shortcuts import render, redirect
from AdminProducts.models import ProductModel
from AdminCategories.models import CategoryModel
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from Products.models import ReviewModel
from django.contrib import messages

# Create your views here.
def load_viewproduct(request,pid):
    productdata = ProductModel.objects.get(product_id = pid)
    similarproducts = ProductModel.objects.filter(subcat_id__cat_id=productdata.subcat_id.cat_id).exclude(product_id=pid)
    # reviewdata=ReviewModel.objects.get(product_id=pid)
    context = {
        # 'reviewdata' : reviewdata,
        'productdata' : productdata,
        'similarproducts' : similarproducts,
    }    
    return render(request,'product/singleproduct.html',context)

def load_ajax_product(request):
    return render(request,'product/shopajax.html')

def load_menuproduct(request, cid=None):
    # 1) start with one queryset and filter it (if cid given)
    qs = ProductModel.objects.all()
    if cid is not None:
        qs = qs.filter(subcat_id__cat_id=cid)

    # 2) optional ordering
    qs = qs.order_by('product_id')

    # 3) paginate the SAME queryset
    paginator = Paginator(qs, 3)              # 12 per page
    page_number = request.GET.get('page')      # None is fine; get_page() handles it
    page_obj = paginator.get_page(page_number)

    # 4) other sidebar data
    catdata = CategoryModel.objects.all()

    return render(request, 'product/user_products.html', {
        'page_obj': page_obj,   # <-- use this in template
        'catdata': catdata,
     })


@csrf_exempt
def load_products(request):
    catid = request.POST.get("catid")
    minvalue = float(request.POST.get("minvalue"))
    maxvalue = float(request.POST.get("maxvalue"))
    
    if catid == "All":
        data = ProductModel.objects.all()
    else:
        data = ProductModel.objects.filter(subcat_id__cat_id=catid)

    if minvalue:
        data = data.filter(sell_price__gte=minvalue)
    if maxvalue:
        data = data.filter(sell_price__lte=maxvalue)

    data = list(data.values())

    return JsonResponse(data,safe=False)
def add_review(request):
    try:
        if request.method == "POST":
            product_id = request.POST.get("product_id")
            user_name = request.POST.get("name")
            user_email = request.POST.get("email")
            review_text = request.POST.get("comment")
            rating = request.POST.get("rating")
            # Create a new review instance
            review = ReviewModel(
                product_id=ProductModel.objects.get(product_id=product_id),
                user_name=user_name,
                user_email=user_email,
                review_text=review_text,
                rating=rating
            )
            review.save()
            messages.success(request, "Subcategory updated!")
    except Exception as e:
            messages.error(request, e)
    return redirect('/view/' + str(product_id))
