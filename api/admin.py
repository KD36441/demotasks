from django.contrib import admin
from .models import product
# Register your models here.

@admin.register(product)
class productAdmin(admin.ModelAdmin):
 list_display=['id','name','price','discount_price','description','size','color','publish_date','slug','published']