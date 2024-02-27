from django.contrib.auth import views as auth_views
from django.urls import path
from django.shortcuts import render
from . import views

app_name ='dashboard'

urlpatterns =[
    path("/dashboard", views.index, name="index"),
] 