# Generated by Django 3.2.9 on 2022-02-06 00:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_animal', models.CharField(max_length=50, verbose_name='Tür')),
                ('genus', models.CharField(max_length=50, verbose_name='Cins')),
                ('name_of_animal', models.CharField(max_length=50, verbose_name='Hayvan Adı')),
                ('age_of_animal', models.PositiveSmallIntegerField(verbose_name='Yaş')),
                ('explanation', models.TextField(verbose_name='Açıklama')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Sahip')),
            ],
        ),
    ]
