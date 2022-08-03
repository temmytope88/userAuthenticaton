from importlib.resources import as_file
from django.contrib import admin
from django.urls import path
from .views import HomeView, LoginView, RegisterView, processRegView

urlpatterns = [
    path('',  HomeView.as_view(), name="home"),
    path('login', LoginView.as_view(), name="login"),
    path('register',  RegisterView.as_view(), name="register"),
    path('regprocess', processRegView.as_view(), name="reg")
]