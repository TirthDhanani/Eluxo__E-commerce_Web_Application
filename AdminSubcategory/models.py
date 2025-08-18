from django.db import models
from AdminCategories.models import CategoryModel

# Create your models here.
class SubcategoryModel(models.Model):
    subcat_id = models.AutoField(primary_key=True)
    subcat_name = models.CharField(max_length=100)
    subcat_image = models.CharField(max_length=100)
    cat_id = models.ForeignKey(CategoryModel,default=None,db_column="cat_id",on_delete=models.CASCADE)

    class Meta:
        db_table = "tbl_subcategory"
         