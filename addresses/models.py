from django.db import models
from common.models import BaseModel

# Create your models here.


class Address(models.Model):
    location = models.CharField(max_length=255)
    postal_address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = "addresses"