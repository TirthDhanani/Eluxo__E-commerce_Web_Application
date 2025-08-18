from django.db import models
from Orders.models import OrderModel
from django.conf import settings

# Create your models here.
class OrderlogModel(models.Model):
    order_id = models.ForeignKey(OrderModel,default=None,related_name='logs_by_order',db_column="order_id",on_delete=models.CASCADE)
    log_id =models.AutoField(primary_key=True)
    status = models.CharField(max_length=50)
    update_dateandtime = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'tbl_orderlogs'