from django.shortcuts import render, redirect
from django.contrib import messages
from .models import SubcategoryModel
from AdminCategories.models import CategoryModel
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings

def admin_subcategory(request):
    subcatdata = SubcategoryModel.objects.all()
    context = {
        "subcatdata":subcatdata
    }
    return render(request, 'admin/subcategory/view_subcategory.html',context)

    
def add_subcategory(request):
    if request.method  == "GET":
        categories = CategoryModel.objects.all()
        context =  {
            'categories' : categories
        }

        return render(request, 'admin/subcategory/add_subcategory.html',context)
    else:
        try:
            file_request = request.FILES['txtsubcatimg']
            fs = FileSystemStorage()
            file = fs.save('subcategory/' +  (file_request.name).replace(" ","_"), file_request)
            fileurl = fs.url(file)


            subcatimg = fileurl
            subcatname = request.POST.get("txtsubcatname")
            catid = request.POST.get('txtcatid')
            
            obj = SubcategoryModel()
            obj.subcat_image = subcatimg
            obj.subcat_name = subcatname
            obj.cat_id = CategoryModel.objects.get(cat_id = catid)
            obj.save()
            messages.success(request, "Subcategory added!")
        except Exception as e:
            messages.error(request, e)
        return redirect('/custom/subcategory/view')
def delete_subcategory(request, sid):
    try:
        obj = SubcategoryModel.objects.get(subcat_id = sid)
        subcatimagepath = obj.subcat_image
        if subcatimagepath.startswith('/media/'):
            subcatimagepath = subcatimagepath[len('/media/'):]
        
        file_path = os.path.join(settings.MEDIA_ROOT, subcatimagepath)
        if os.path.isfile(file_path):
            os.remove(file_path)
        obj.delete()
        messages.success(request, "Subcategory deleted!")
    except Exception as e:
        messages.error(request, e)
    return redirect("/custom/subcategory/view")

def edit_subcategory(request,sid):
    if request.method == "GET":
        categories = CategoryModel.objects.all()
        subcatdata = SubcategoryModel.objects.get(subcat_id = sid)
        context =  {
            'categories' : categories,
            "subcatdata":subcatdata
        }
        return render(request, 'admin/subcategory/edit_subcategory.html',context)
    else:
        try:
            obj = SubcategoryModel.objects.get(subcat_id = sid)
            subcatname = request.POST.get("txtsubcatname")
            catid = request.POST.get('txtcatid')
            obj.subcat_name = subcatname
            obj.cat_id = CategoryModel.objects.get(cat_id = catid)



            request_file = request.FILES['txtsubcatimg'] if 'txtsubcatimg' in request.FILES else None
            if request_file:
                #REMOVE OLD IMAGE
                subcatimagepath = obj.subcat_image
                if subcatimagepath.startswith('/media/'):
                    subcatimagepath = subcatimagepath[len('/media/'):]
                
                file_path = os.path.join(settings.MEDIA_ROOT, subcatimagepath)
                if os.path.isfile(file_path):
                    os.remove(file_path)

                #UPLOAD NEW IMAGE
                file_request = request.FILES['txtsubcatimg']
                fs = FileSystemStorage()
                file = fs.save('subcategory/' +  (file_request.name).replace(" ","_"), file_request)
                fileurl = fs.url(file)
                subcatimg = fileurl
                obj.subcat_image = subcatimg
                
            obj.save()
            messages.success(request, "Subcategory updated!")
        except Exception as e:
            messages.error(request, e)
        return redirect('/custom/subcategory/view')


