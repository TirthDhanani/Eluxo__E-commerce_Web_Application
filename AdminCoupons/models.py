from django.db import models

# Create your models here.
class CouponModel(models.Model):
    coupon_id = models.AutoField(primary_key=True)
    coupon_code = models.CharField(max_length=100)
    min_cart_value = models.IntegerField()
    max_cart_value = models.IntegerField()
    discount_percent = models.IntegerField()
    coupon_stat = models.CharField(max_length=100)

    class Meta:
        db_table = "tbl_coupon" 