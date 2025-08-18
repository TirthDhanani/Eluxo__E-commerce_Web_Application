from django.db import models
from AdminSubcategory.models import SubcategoryModel

# Create your models here.
class ProductModel(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    product_specification = models.TextField()
    retail_price = models.IntegerField()
    sell_price = models.IntegerField()
    thumbnail_image = models.CharField(max_length=100)
    image1 = models.CharField(max_length=100)
    image2 = models.CharField(max_length=100)
    image3 = models.CharField(max_length=100)
    Video_url = models.CharField(max_length=100)
    subcat_id = models.ForeignKey(SubcategoryModel,default=None,db_column="subcat_id",on_delete=models.CASCADE)
    is_active = models.CharField(max_length=100)

    class Meta:
        db_table = "tbl_products"
    