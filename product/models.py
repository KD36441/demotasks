from django.db import models
from django.db import models


class Product(models.Model):
	CATEGORY = (
			('kurta', 'kurta'),
			('jeans', 'jeans'),
			) 
    
	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	discount=models.IntegerField(null=False,default=0)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True, blank=True)
	colour=models.CharField(max_length=15)
	size=models.PositiveIntegerField()
	

	def __str__(self):
		return self.name



