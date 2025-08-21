from django.db import models
from AdminProducts.models import ProductModel
# Create your models here.
class ReviewModel(models.Model):
    review_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(ProductModel, default=None, db_column="product_id", on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=100)
    review_text = models.TextField()
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta :
        db_table = 'tbl_reviews'


