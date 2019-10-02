from rest_framework import serializers
from . models import Product,Review
class ProductSerializer (serializers.ModelSerializer):
     class Meta:
         model = Product
         fields = ('p_id','p_name','p_cost','p_mfd','p_exd')

class ReviewSerializer (serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id','title','review','ratings','created_by')