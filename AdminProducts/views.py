from django.shortcuts import render,redirect
from .models import ProductModel
from AdminSubcategory.models import SubcategoryModel
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



def getAllProducts(request):
    productdata = ProductModel.objects.all().values()
    data = list(productdata)
    return JsonResponse(data,safe=False)

@csrf_exempt
def create_product(request):
    try:
        #thumbnail image
        thumbnail_image = request.FILES['thumbnail_image']
        fs = FileSystemStorage()
        file = fs.save('products/' +  (thumbnail_image.name).replace(" ","_"), thumbnail_image)
        thumbnail_image_url = fs.url(file)
        thumbnailimg = thumbnail_image_url
        #product image 1
        image_1 = request.FILES['image_1']
        file1 = fs.save('products/' +  (image_1.name).replace(" ","_"), image_1)
        image_1_url = fs.url(file1)
        image1 = image_1_url
        #product image 2
        image_2 = request.FILES['image_2']
        file2 = fs.save('products/' +  (image_2.name).replace(" ","_"), image_2)
        image_2_url = fs.url(file2)
        image2 = image_2_url
        #product image 3
        image_3 = request.FILES['image_3']
        file3 = fs.save('products/' +  (image_3.name).replace(" ","_"), image_3)
        image_3_url = fs.url(file3)
        image3 = image_3_url
        productname =  request.POST.get('product_name')
        productdescription =  request.POST.get('description')
        productspecifications =  request.POST.get('specifications')
        productretailprice =  request.POST.get('retail_price')
        productsellprice =  request.POST.get('sell_price')
        productvideourl =  request.POST.get('video_url')
        productstatus = request.POST.get('product_status')
        subcatid = request.POST.get('subcat_id')

        obj = ProductModel()
        obj.product_name = productname
        obj.product_description = productdescription
        obj.product_specification = productspecifications
        obj.retail_price = productretailprice
        obj.sell_price = productsellprice
        obj.Video_url = productvideourl
        obj.is_active = productstatus
        obj.thumbnail_image = thumbnailimg
        obj.image1 = image1
        obj.image2 = image2
        obj.image3 = image3
        obj.subcat_id = SubcategoryModel.objects.get(subcat_id = subcatid)
        obj.save()
        return JsonResponse({"status":True,"message":"Product Created"},safe=False)
    except Exception as e:
        return JsonResponse({"status":False,"message":str(e)},safe=False)
  


# Create your views here.
def view_products(request):
    productdata = ProductModel.objects.all()
    context = {
        'productdata' : productdata
    }
    return render(request, 'admin/products/view_products.html', context)
def add_products(request):
    if request.method == "GET":
        subcategories = SubcategoryModel.objects.all()
        context = {
            'subcategories' : subcategories
        }
        return render(request, 'admin/products/add_products.html', context)
    else:
        try:
            #thumbnail image
            thumbnail_image = request.FILES['thumbnail_image']
            fs = FileSystemStorage()
            file = fs.save('products/' +  (thumbnail_image.name).replace(" ","_"), thumbnail_image)
            thumbnail_image_url = fs.url(file)
            thumbnailimg = thumbnail_image_url
            #product image 1
            image_1 = request.FILES['image_1']
            file1 = fs.save('products/' +  (image_1.name).replace(" ","_"), image_1)
            image_1_url = fs.url(file1)
            image1 = image_1_url
            #product image 2
            image_2 = request.FILES['image_2']
            file2 = fs.save('products/' +  (image_2.name).replace(" ","_"), image_2)
            image_2_url = fs.url(file2)
            image2 = image_2_url
            #product image 3
            image_3 = request.FILES['image_3']
            file3 = fs.save('products/' +  (image_3.name).replace(" ","_"), image_3)
            image_3_url = fs.url(file3)
            image3 = image_3_url
            productname =  request.POST.get('product_name')
            productdescription =  request.POST.get('description')
            productspecifications =  request.POST.get('specifications')
            productretailprice =  request.POST.get('retail_price')
            productsellprice =  request.POST.get('sell_price')
            productvideourl =  request.POST.get('video_url')
            productstatus = request.POST.get('product_status')
            subcatid = request.POST.get('subcat_id')

            obj = ProductModel()
            obj.product_name = productname
            obj.product_description = productdescription
            obj.product_specification = productspecifications
            obj.retail_price = productretailprice
            obj.sell_price = productsellprice
            obj.Video_url = productvideourl
            obj.is_active = productstatus
            obj.thumbnail_image = thumbnailimg
            obj.image1 = image1
            obj.image2 = image2
            obj.image3 = image3
            obj.subcat_id = SubcategoryModel.objects.get(subcat_id = subcatid)
            obj.save()
            messages.success(request, "Product added!")
        except Exception as e:
            messages.error(request, e)
        return redirect('/custom/products/view')   
            
            


def delete_products(request, pid):
    try:
        obj = ProductModel.objects.get(product_id = pid)
        # delete thumbnail image from the media file 
        thumbnailimgpath = obj.thumbnail_image
        if thumbnailimgpath.startswith('/media/'):
            thumbnailimgpath = thumbnailimgpath[len('/media/'):]
        thumbnailimg_path = os.path.join(settings.MEDIA_ROOT, thumbnailimgpath)
        if os.path.isfile(thumbnailimg_path):
            os.remove(thumbnailimg_path)
        # delete image 1 from the media file 
        image1path = obj.image1
        if image1path.startswith('/media/'):
            image1path = image1path[len('/media/'):]
        image1_path = os.path.join(settings.MEDIA_ROOT, image1path)
        if os.path.isfile(image1_path):
            os.remove(image1_path)
        # delete image 2 from the media file 
        image2path = obj.image2
        if image2path.startswith('/media/'):
            image2path= image2path[len('/media/'):]
        image2_path = os.path.join(settings.MEDIA_ROOT, image2path)
        if os.path.isfile(image2_path):
            os.remove(image2_path)
        # delete image 3 from the media file 
        image3path = obj.image3
        if image3path.startswith('/media/'):
            image3path= image3path[len('/media/'):]
        image3_path = os.path.join(settings.MEDIA_ROOT, image3path)
        if os.path.isfile(image3_path):
            os.remove(image3_path)
        obj.delete()
        messages.success(request,'Product deleted successfully!')
    except Exception as e:
        messages.error(request, e)

    return redirect("/custom/products/view")
def edit_products(request, pid):
    if request.method == "GET":
        subcategories = SubcategoryModel.objects.all
        productdata = ProductModel.objects.get(product_id = pid)
        context = {
            'subcat' : subcategories,
            'productdata' : productdata
        }
        return render(request, 'admin/products/edit_products.html', context)
    else:
        try:
            obj = ProductModel.objects.get(product_id = pid)
            productname =  request.POST.get('product_name')
            productdescription =  request.POST.get('description')
            productspecifications =  request.POST.get('specifications')
            productretailprice =  request.POST.get('retail_price')
            productsellprice =  request.POST.get('sell_price')
            productvideourl =  request.POST.get('video_url')
            productstatus = request.POST.get('product_status')
            subcatid = request.POST.get('subcat_id')

            fs = FileSystemStorage()

            #thumbnail image
            request_thumbnail_image = request.FILES['thumbnail_image'] if "thumbnail_image" in request.FILES else None
            if request_thumbnail_image: 
                thumbnailimgpath = obj.thumbnail_image
                if thumbnailimgpath.startswith('/media/'):
                    thumbnailimgpath = thumbnailimgpath[len('/media/'):]
                thumbnailimg_path = os.path.join(settings.MEDIA_ROOT, thumbnailimgpath)
                if os.path.isfile(thumbnailimg_path):
                    os.remove(thumbnailimg_path)
                thumbnail_image = request.FILES['thumbnail_image']
                
                file = fs.save('products/' +  (thumbnail_image.name).replace(" ","_"), thumbnail_image)
                thumbnail_image_url = fs.url(file)
                thumbnailimg = thumbnail_image_url
                obj.thumbnail_image = thumbnailimg
            #product image 1
            request_image1 = request.FILES['image_1'] if 'image_1' in request.FILES else None
            if request_image1:
                # delete image 1 from the media file 
                image1path = obj.image1
                if image1path.startswith('/media/'):
                    image1path = image1path[len('/media/'):]
                image1_path = os.path.join(settings.MEDIA_ROOT, image1path)
                if os.path.isfile(image1_path):
                    os.remove(image1_path)
                image_1 = request.FILES['image_1']
                file1 = fs.save('products/' +  (image_1.name).replace(" ","_"), image_1)
                image_1_url = fs.url(file1)
                image1 = image_1_url
                obj.image1 = image1
            #product image 2
            request_image2 = request.FILES['image_2'] if 'image_2' in request.FILES else None
            if request_image2:
                # delete image 2 from the media file 
                image2path = obj.image2
                if image2path.startswith('/media/'):
                    image2path = image2path[len('/media/'):]
                image2_path = os.path.join(settings.MEDIA_ROOT, image2path)
                if os.path.isfile(image2_path):
                    os.remove(image2_path)
                image_2 = request.FILES['image_2']
                file2 = fs.save('products/' +  (image_2.name).replace(" ","_"), image_2)
                image_2_url = fs.url(file2)
                image2 = image_2_url
                obj.image2 = image2
            #product image 3
            request_image3 = request.FILES['image_3'] if 'image_3' in request.FILES else None
            if request_image3:
                # delete image 3 from the media file 
                image3path = obj.image3
                if image3path.startswith('/media/'):
                    image3path = image3path[len('/media/'):]
                image3_path = os.path.join(settings.MEDIA_ROOT, image3path)
                if os.path.isfile(image3_path):
                    os.remove(image3_path)
                image_3 = request.FILES['image_3']
                file3 = fs.save('products/' +  (image_3.name).replace(" ","_"), image_3)
                image_3_url = fs.url(file3)
                image3 = image_3_url
                obj.image3 = image3
            
            obj.product_name = productname
            obj.product_description = productdescription
            obj.product_specification = productspecifications
            obj.retail_price = productretailprice
            obj.sell_price = productsellprice
            obj.Video_url = productvideourl
            obj.is_active = productstatus
            
            obj.subcat_id = SubcategoryModel.objects.get(subcat_id = subcatid)
            obj.save()
            messages.success(request, 'Product updated successfully!')
        except Exception as e:
            messages.error(request, e)
        return redirect('/custom/products/view')

    


