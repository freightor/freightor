import os
import uuid
from django.db import models
from django.contrib.auth.models import User
from common.models import BaseModel
from addresses.models import Address
from accounts.models import Profile
from companies.models import Employee

# Create your models here.


def store_logos(instance, filename):
    file_ext = os.path.splitext(filename)[1]
    return "logos/stores/store_{0}{1}".format(instance.id, file_ext)


class Store(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    logo = models.ImageField(upload_to=store_logos,null=True,blank=True)
    name = models.CharField(max_length=255)
    address = models.ForeignKey(
        Address, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    rating = models.DecimalField(default=0, decimal_places=1, max_digits=2)
    verified = models.BooleanField(default=False)


class Merchant(BaseModel, Profile):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    store = models.ForeignKey(
        Store, on_delete=models.CASCADE, null=True, blank=True)


class Album(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(null=True, blank=True, max_length=100)


def get_upload_directory(instance, filename):
    file_ext = os.path.splitext(filename)[1]
    return "album_{0}/pic_{1}{2}".format(instance.album.id, instance.id, file_ext)


class Picture(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    attachment = models.ImageField(upload_to=get_upload_directory)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)


class Category(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    parent_category = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(default="others")

    class Meta:
        verbose_name_plural = "categories"


def cover_image_location(instance, filename):
    file_ext = os.path.splitext(filename)[1]
    return "covers/store_{0}/product_{1}{2}".format(instance.store.id, instance.id, file_ext)


class Product(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    new_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.IntegerField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to=cover_image_location,null=True,blank=True)
    album = models.OneToOneField(
        Album, on_delete=models.CASCADE, null=True, blank=True)


class Order(BaseModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through="OrderItem")
    total_amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
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
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
