from django.contrib.auth import views as auth_views
from django.urls import path
from django.shortcuts import render
from .forms import LoginForm
from . import views


app_name ='core'

urlpatterns =[
    path("", views.index, name="index"),
    path("signup/", views.signup , name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name="core/login.html", authentication_form = LoginForm), name="login"),
    path("logout/", views.logout_view, name="logout")
] 