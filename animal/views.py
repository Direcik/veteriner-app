from django.shortcuts import render, redirect, get_object_or_404
from .forms import AnimalForm, AnimalFormAdmin
from .models import Animal
from django.contrib import messages
from django.contrib.auth.models import User
from users.models import MyUserModel


def index(request):
    return render(request, "index.html")

def dashboard(request):
    keyword = request.GET.get("keyword")
    if keyword:
        if request.user.is_superuser:
            animals = Animal.objects.filter(name_of_animal__contains=keyword)
        else:
            animals = Animal.objects.filter(owner=request.user,name_of_animal__contains=keyword)
        return render(request, "dashboard.html", {"animals": animals})

    if request.user.is_superuser:
        animals = Animal.objects.filter()
        context = {
            "animals": animals        
        }
    else:
        animals = Animal.objects.filter(owner = request.user)
        context = {
            "animals": animals        
        }
    return render(request, "dashboard.html", context)

def addAnimal(request):
    if request.user.is_superuser:
        form = AnimalFormAdmin(request.POST or None, request.FILES or None)
        if form.is_valid():
            animal = form.save()
            animal.save()
            messages.success(request, "Hayvan Ekleme Başarılı")
            return redirect("animal:dashboard")
    else:
        form = AnimalForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            animal = form.save(commit = False)
            animal.owner = request.user
            animal.save()
            messages.success(request, "Hayvan Ekleme Başarılı")
            return redirect("animal:dashboard")

    return render(request, "addanimal.html", {"form":form})

def updateAnimal(request, id):
    animal = get_object_or_404(Animal, id=id)
    form = AnimalForm(request.POST or None, request.FILES or None, instance=animal)
    if form.is_valid():
        if request.user.is_superuser:
            animal = form.save()
            animal.save()
        else:
            animal = form.save(commit = False)
            animal.owner = request.user
            animal.save()
        messages.success(request, '{} Güncellendi.'.format(animal.name_of_animal))
        return redirect("animal:dashboard")
    return render(request, "update.html", {'form': form})

def deleteAnimal(request, id):
    if request.user.is_superuser:
        animal = get_object_or_404(Animal, id=id)
        animal.delete()
        messages.success(request, "{} Silindi.".format(animal.name_of_animal))
        return redirect("animal:dashboard")
    else:
        messages.info(request, "Bu işlem için yetkiniz bulunmamaktadır.")
        return redirect("animal:dashboard")

