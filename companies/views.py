from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from companies.models import Employee, Employer
from companies.forms import EmployeeForm

# Create your views here.


def new_employee(request):
    employer = request.user.employee.employer
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        temp = "{0}@{1}".format(form.first_name[::-1], form.last_name[::-1])
        form.password1, form.password2 = temp
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            new_guy = Employee(user=user, employer=employer,
                               user_type="employee")
            new_guy.created_by = request.user
            new_guy.save()
            return redirect("companies:employee_detail")
    else:
        form = EmployeeForm()
    return render(request, "companies/new_employee.html", {"form": form})
