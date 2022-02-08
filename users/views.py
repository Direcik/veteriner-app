from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from users.models import MyUserModel
from django.contrib.auth import login, authenticate, logout

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")
        email = form.cleaned_data.get("email")
        address = form.cleaned_data.get("address")
        phone_number = form.cleaned_data.get("phone_number")

        newUser = MyUserModel(username=username, first_name=first_name, last_name=last_name,email=email,address=address,phone_number=phone_number)
        newUser.set_password(password)
        newUser.save()
        login(request, newUser)
        messages.success(request, "Kayıt İşlemi Başarılı")
        return redirect("index")
    context = {
        "form": form
    }
    return render(request, "register.html", context)


def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        
        if user is None:
            messages.info(request, "Kullanıcı Adı veya Parola Hatalı")
            return render(request, "login.html", context)
        
        messages.success(request, "Giriş İşlemi Başarılı")
        login(request, user)
        return redirect("index")
    return render(request, "login.html", context)

def logoutUser(request):
    logout(request)
    messages.success(request, "Çıkış İşlemi Başarılı")
    return redirect("index")