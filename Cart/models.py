from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from AdminProducts.models import ProductModel

class CartModel(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product_id = models.ForeignKey(ProductModel,default=None,db_column="product_id",on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        db_table = 'tbl_cart'

        
    def getproducttotal(self):
        return float(self.quantity) * float(self.product_id.sell_price)