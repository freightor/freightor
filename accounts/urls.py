from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views

app_name = "accounts"
urlpatterns = [
    path("login/", auth_views.login, {
         "template_name": "accounts/login.html"}, name="login"),
    path("logout/", auth_views.logout, {
         "next_page": "/accounts/login"}, name="logout"),
    path("signup/<str:user_type>/", views.signup, name="signup"),
]
