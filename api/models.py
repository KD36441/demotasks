from contextlib import suppress
from tabnanny import verbose
from datetime import datetime
from time import time
from turtle import color
from django.db import models
from pytz import timezone



CHOOSE_SIZE = (
('Extra Small', 'XS'),
('Small', 'S'),
('Medium', 'M'),
('Large', 'L'),
('Extra Large', 'XL'),
('Double Large', 'XXL'),
('Triple Large', 'XXXL'),
)

class product(models.Model):
    name=models.CharField(max_length=30,null=False)
    price = models.DecimalField(decimal_places=2,max_digits=1000)
    discount_price=models.IntegerField(null=False,default=0)
    description = models.TextField(blank=True, null=True)
    size = models.CharField(max_length=120, choices=CHOOSE_SIZE)
    color=models.CharField(max_length=15)
    publish_date=models.DateTimeField(auto_now=True,blank=False,null=False)
    slug=models.SlugField(max_length=225,default='')
    published=models.BooleanField(default=True)


    def __str__(self):
      return self.name

   
      
      
      

    
      