from django.db import models
from django.contrib.auth.models import User
from common.models import BaseModel
from addresses.models import Address
from accounts.models import Profile

# Create your models here.


class Employer(BaseModel):
    logo = models.ImageField()
    name = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    description = models.TextField()


class Employee(BaseModel, Profile):
    salary = models.FloatField(null=True, blank=True)
    address = models.ForeignKey(
        Address, on_delete=models.CASCADE, null=True, blank=True)
    employer = models.ForeignKey(
        Employer, on_delete=models.CASCADE, null=True, blank=True)
    employee_no = models.CharField(
        max_length=30, unique=True, null=True, blank=True)
