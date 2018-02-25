from django.contrib import admin
from companies.models import Employee, Employer

# Register your models here.
admin.site.register(Employee)
admin.site.register(Employer)