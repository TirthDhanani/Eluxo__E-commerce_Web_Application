from django.db import models
from django.db.models import Count

# Create your models here.
class CategoryModel(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=100)
    cat_image = models.CharField(max_length=100)
    


    class Meta:
        db_table = "tbl_category" 

    
    def product_count(self):
        from AdminProducts.models import ProductModel
        return ProductModel.objects.filter(subcat_id__cat_id_id=self.cat_id).count()  

