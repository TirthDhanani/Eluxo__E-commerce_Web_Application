from rest_framework import serializers
from .models import CouponModel  # adjust import to your app

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = CouponModel
        fields = '__all__'  # or list fields explicitly
        read_only_fields = ['coupon_id',]  # tweak as needed