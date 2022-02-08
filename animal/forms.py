from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['type_of_animal', 'genus', 'name_of_animal', 'age_of_animal', 'explanation']

class AnimalFormAdmin(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['owner','type_of_animal', 'genus', 'name_of_animal', 'age_of_animal', 'explanation']
