from django.db import models

# Create your models here.


class Stock(models.Model):
    types = models.CharField(max_length=100)

    def __str__(self):
        return self.types


class Country(models.Model):
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.country


class Item(models.Model):
    stock = models.ForeignKey(Stock, null=True, on_delete=models.SET_NULL)
    country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100)
    types = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField(blank=True, default="Image URL")
    image = models.ImageField(blank=True, default="IMAGE")
    objects = models.Manager()

    def __str__(self):
        return self.name
