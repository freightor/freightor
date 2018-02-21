from django.db import models
from common.models import BaseModel
from addresses.models import Address

# Create your models here.


class Merchant(BaseModel):
    logo = models.ImageField()
    name = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    description = models.TextField()
    rating = models.FloatField()


class Album(BaseModel):
    name = models.CharField(null=True, blank=True)


class Picture(BaseModel):
    filename = models.FileField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)


class Category(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    parent_category = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True)


class Item(BaseModel):
    name = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    description = models.TextField()
    old_price = models.FloatField()
    new_price = models.FloatField()
    quantity_in_stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
