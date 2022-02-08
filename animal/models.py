from django.db import models
from users.models import MyUserModel

class Animal(models.Model):
    owner = models.ForeignKey("users.MyUserModel", on_delete=models.CASCADE, verbose_name="Sahip Username")
    type_of_animal = models.CharField(max_length=50, verbose_name="Tür")
    genus = models.CharField(max_length=50, verbose_name="Cins")
    name_of_animal = models.CharField(max_length=50, verbose_name="Hayvan Adı")
    age_of_animal = models.PositiveSmallIntegerField(verbose_name="Yaş")
    explanation = models.TextField(verbose_name="Açıklama")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.owner)
