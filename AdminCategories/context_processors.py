from .models import CategoryModel
def navbar_categories(request):
    data = CategoryModel.objects.all()
    return {"catdata":data}
    