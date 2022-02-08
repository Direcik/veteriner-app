from django.contrib import admin
from django.urls import path
from . import views

app_name = "animal"

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('addanimal/', views.addAnimal, name="addanimal"),
    path('update/<int:id>', views.updateAnimal, name="update"),
    path('delete/<int:id>', views.deleteAnimal, name="delete"),
]