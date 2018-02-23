from django.contrib.auth.forms import UserCreationForm


class EmployeeForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
