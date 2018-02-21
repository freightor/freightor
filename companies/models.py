from django.db import models
from common.models import BaseModel
from addresses.models import Address

# Create your models here.


class Employer(BaseModel):
    logo = models.ImageField()
    name = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    description = models.TextField()


class Employee(BaseModel):
    avatar = models.ImageField()
    name = models.CharField(max_length=255)
    salary = models.FloatField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    company = models.ForeignKey(Employer, on_delete=models.CASCADE)
    employee_no = models.CharField(max_length=30, unique=True)
