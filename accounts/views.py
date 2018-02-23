from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from accounts.forms import SignUpForm
from companies.models import Employee
from shop.models import Merchant

# Create your views here.


def signup(request, user_type):
    print(user_type)
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            if user_type == "employee":
                Employee.objects.create(
                    user=user, role="admin", user_type="employee")
                return redirect("companies:new_employer")
            Merchant.objects.create(
                user=user, role="admin", user_type="merchant")
            return redirect("shop:new_store")
    else:
        form = SignUpForm()
    return render(request, "accounts/signup.html", {"form": form})
