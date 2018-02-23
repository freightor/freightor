from django.db import models
from django.contrib.auth.models import User
from common.models import BaseModel
from addresses.models import Address
from accounts.models import Profile
from companies.models import Employee

# Create your models here.


class Store(BaseModel):
    logo = models.FileField()
    name = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    description = models.TextField()
    rating = models.FloatField()


class Merchant(BaseModel, Profile):
    store = models.ForeignKey(
        Store, on_delete=models.CASCADE, null=True, blank=True)


class Album(models.Model):
    name = models.CharField(null=True, blank=True, max_length=100)


def get_upload_directory(instance, filename):
    import os
    file_ext = os.path.splitext(filename)[1]
    return "album_{1}/pic_{2}{3}".format(instance.album.id, instance.id, file_ext)


class Picture(models.Model):
    attachment = models.ImageField(upload_to=get_upload_directory)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)


class Category(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    parent_category = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField()


class Product(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    old_price = models.DecimalField()
    new_price = models.DecimalField()
    quantity_in_stock = models.IntegerField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    album = models.OneToOneField(Album, on_delete=models.CASCADE)


class Order(BaseModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through="OrderItem")
    total_amount = models.DecimalField(null=True, blank=True)
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("on_hold", "On Hold"),
        ("processing", "Processing"),
        ("in_transit", "In Transit"),
        ("delivered", "Delivered")
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="pending")


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    unit_price = models.DecimalField()
    price = models.DecimalField()
