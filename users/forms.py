from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyUserModel

class MyUserModelUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = MyUserModel()
        fields = ('username', 'email', 'address', 'phone_number')

class MyUserModelUserChangeForm(UserChangeForm):
    class Meta:
        model = MyUserModel
        fields = ('username', 'email', 'address', 'phone_number')

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label="Kullanıcı Adı")
    password = forms.CharField(max_length=20, label="Parola", widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20, label="Parola Doğrula", widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=50, label="Adınız")
    last_name = forms.CharField(max_length=50, label="Soyadınız")
    email = forms.EmailField(max_length=255, label="Email Adresiniz")
    address = forms.CharField(max_length=255, label = "Adresiniz")
    phone_number = forms.CharField(max_length=13, label='Telefon Numaranız')

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        email = self.cleaned_data.get("email")
        address = self.cleaned_data.get("address")
        phone_number = self.cleaned_data.get("phone_number")


        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolalar Eşleşmiyor.")

        values = {
            "username": username,
            "password": password,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "address": address,
            "phone_number": phone_number,
        }
        return values


class LoginForm(forms.Form):
    username = forms.CharField(label = "Kullanıcı Adı")
    password = forms.CharField(label = "Parola", widget=forms.PasswordInput)