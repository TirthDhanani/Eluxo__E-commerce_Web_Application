from django.shortcuts import render
from AdminProducts.models import ProductModel
from AdminCategories.models import CategoryModel
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
# Create your views here.
def load_viewproduct(request,pid):
    productdata = ProductModel.objects.get(product_id = pid)
    context = {
        'productdata' : productdata
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
    # # Pagination
    # paginator = Paginator(data, per_page)
    # page_obj = paginator.get_page(data)

    # # Build JSON rows (avoid serializing model instances)
    # items = []
    # for p in page_obj.object_list:
    #     # If these are FileFields/ImageFields, .url gives a usable src
    #     thumb_url = getattr(p.thumbnail_image, 'url', '') if hasattr(p, 'thumbnail_image') else ''
    #     image2_url = getattr(p.image2, 'url', '') if hasattr(p, 'image2') else thumb_url
    #     items.append({
    #         "product_id": p.pk,
    #         "product_name": getattr(p, "product_name", str(p)),
    #         "sell_price": str(getattr(p, "sell_price", "0")),  # keep as string for JSON safety
    #         "thumbnail_image": thumb_url,
    #         "image2": image2_url,
    #     })

    # # Compact page range with ellipsis
    # elided = page_obj.paginator.get_elided_page_range(
    #     number=page_obj.number, on_each_side=1, on_ends=1
    # )
    # pages = [n if isinstance(n, int) else "…" for n in elided]

    # return JsonResponse({
    #     "items": items,
    #     "pagination": {
    #         "page": page_obj.number,
    #         "num_pages": paginator.num_pages,
    #         "has_next": page_obj.has_next(),
    #         "has_previous": page_obj.has_previous(),
    #         "next_page": page_obj.next_page_number() if page_obj.has_next() else None,
    #         "prev_page": page_obj.previous_page_number() if page_obj.has_previous() else None,
    #         "pages": pages,
    #         "total": paginator.count,
    #     }
    # })
    return JsonResponse(data,safe=False)
