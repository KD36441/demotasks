from rest_framework import serializers
from .models import product

class productSerializer(serializers.ModelSerializer):
 class Meta:
  model = product
  fields = ['id','name','price','discount_price','description','size','color','publish_date','slug','published']