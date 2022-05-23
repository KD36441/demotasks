from django.contrib import admin
from dataclasses import fields
from itertools import product
from pyexpat import model
from django.contrib import admin
from .models import Product

@admin.register(Product)

class Productadmin(admin.ModelAdmin):
    class meta:
     model=Product
     fields=['name','price','discount','category','description','colour','size']
       


        



