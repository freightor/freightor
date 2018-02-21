from django.db import models
from common.models import BaseModel

# Create your models here.


class Address(BaseModel):
    location = models.CharField(max_length=255)
    postal_address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
