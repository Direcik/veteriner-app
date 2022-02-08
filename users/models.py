from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUserModel(AbstractUser):
    address = models.CharField(max_length=255, verbose_name="Adres")
    phone_number = models.CharField(max_length=13, verbose_name="Telefon Numarası")

    def __str__(self):
        return self.username
