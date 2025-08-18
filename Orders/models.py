from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from AdminProducts.models import ProductModel
# Create your models here.
class OrderModel(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    total_payment = models.IntegerField()
    discount = models.IntegerField(default=0) 
    state = models.CharField(max_length=20)
    city =  models.CharField(max_length=20)
    addressline1 = models.CharField(max_length=100)
    addressline2=models.CharField(max_length=100)
    pincode = models.IntegerField()
    status = models.CharField(max_length=20, default='Pending')
    orderdatetime = models.DateTimeField(auto_now_add=True)
    contactnumber = models.CharField(max_length=10, default= None)
    class Meta:
       db_table = 'tbl_order'





class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    order_id  = models.ForeignKey(OrderModel, on_delete=models.CASCADE,default=None)
    product_id = models.ForeignKey(ProductModel,default=None,db_column="product_id",on_delete=models.CASCADE)
    quantity = models.IntegerField()
    item_price = models.IntegerField()
    
    class Meta:
        db_table = 'tbl_items'
    def totalofitem(self):
        return float(self.quantity) * float(self.item_price)
        





