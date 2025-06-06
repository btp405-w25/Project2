# Generated by Django 5.1.8 on 2025-04-02 12:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('season', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('ingredients', models.TextField()),
                ('instructions', models.TextField()),
                ('dietary_preferences', models.CharField(choices=[('vegan', 'Vegan'), ('vegetarian', 'Vegetarian'), ('gluten-free', 'Gluten-Free'), ('none', 'No Preference')], max_length=50)),
                ('carbon_footprint', models.FloatField()),
                ('main_ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.ingredient')),
            ],
        ),
    ]
