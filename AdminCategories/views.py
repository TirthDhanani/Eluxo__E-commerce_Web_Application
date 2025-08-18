from django.shortcuts import render,redirect
from .models import CategoryModel
from django.contrib import messages
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
# Create your views here.
def load_admin_categories(request):
    data = CategoryModel.objects.all()
    context = {
        "catdata":data
    }
    return render(request, 'admin/category/view_category.html',context)





def load_add_category(request):
    if request.method == "GET":

        return render(request, 'admin/category/add_category.html')
    else:
        #insert code
        try:
            #ImageUpload
            request_file = request.FILES['txtcatimg']
            fs = FileSystemStorage()
            file = fs.save("category/" + (request_file.name).replace(" ","_"), request_file)
            fileurl = fs.url(file)



            catname = request.POST.get("txtcatname")
            catimage = fileurl
            obj = CategoryModel()
            obj.cat_name = catname
            obj.cat_image = catimage
            obj.save()
            messages.success(request, "Category added!")
        except Exception as e:
            messages.error(request, e)
        return redirect("/custom/category/view")


def delete_category(request,cid):
    try:
        obj = CategoryModel.objects.get(cat_id = cid)
        catimagepath = obj.cat_image
        if catimagepath.startswith('/media/'):
            catimagepath = catimagepath[len('/media/'):]

        
        file_path = os.path.join(settings.MEDIA_ROOT, catimagepath)
       # return HttpResponse(file_path)
        if os.path.isfile(file_path):
                os.remove(file_path)
        obj.delete()
        messages.success(request, "Category deleted!")
    except Exception as e:
        messages.error(request, e)
    return redirect("/custom/category/view")
def edit_category(request,cid):
    if request.method == "GET":
        category = CategoryModel.objects.get(cat_id = cid)
        context =  {
            'category' : category,
            
        }
        return render(request, 'admin/category/edit_category.html',context)
    else:
        try:
            obj = CategoryModel.objects.get(cat_id = cid)
            catname = request.POST.get("txtcatname")
            obj.cat_name = catname
            request_file = request.FILES['txtcatimg'] if 'txtcatimg' in request.FILES else None
            if request_file:
                catimagepath = obj.cat_image
                if catimagepath.startswith('/media/'):
                    catimagepath = catimagepath[len('/media/'):]
                file_path = os.path.join(settings.MEDIA_ROOT, catimagepath)
            # return HttpResponse(file_path)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                
                request_file = request.FILES['txtcatimg']
                fs = FileSystemStorage()
                file = fs.save("category/" + (request_file.name).replace(" ","_"), request_file)
                fileurl = fs.url(file)
                catimage = fileurl
                obj.cat_image = catimage
            obj.save()
            messages.success(request, "Category editted successfully")
        except Exception as e :
            messages.error(request, e)
        return redirect('/custom/category/view')
        
            

        

        


