from django.db import models

# Create your models here.
class Product(models.Model):

	name = models.CharField(max_length=20,null=True)
	quantity = models.CharField(max_length=20,null=True)
	price = models.CharField(max_length=20, null=True)
	def __str__(self):
		return self.name


class Customer(models.Model):

	name = models.CharField(max_length=20, null=True)
	phone = models.CharField(max_length=12, null=True)
	email = models.EmailField(max_length=254)
	address = models.TextField()
	def __str__(self):
		return self.name