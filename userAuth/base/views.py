from ast import Return
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User
from base.models import MyUsers

# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, "base/index.html")

class LoginView(View):
    def get(self, request):
        return render(request, "base/login.html")

class RegisterView(View):
    def get(self, request):
        return render(request, "base/register.html")

class processRegView(View):
    def post(self, request):
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            firstname = request.POST["firstname"]
            lastname = request.POST["lastname"]
            email = request.POST["email"]
            myuser = MyUsers.object.create_user(firstname, lastname, email, password, username)
            myuser.save()
            return redirect("login")
