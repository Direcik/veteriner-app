from django.contrib import admin
from .models import Animal

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['owner', 'type_of_animal', 'genus', 'name_of_animal', 'age_of_animal', 'explanation', 'created_date']
    list_display_links = ['owner', 'name_of_animal']
    search_fields = ['owner', 'name_of_animal']
    list_filter = ['owner', 'name_of_animal']
    class Meta:
        model = Animal