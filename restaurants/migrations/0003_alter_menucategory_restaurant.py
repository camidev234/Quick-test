# Generated by Django 5.0.4 on 2025-01-13 03:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_menucategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menucategory',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_categories', to='restaurants.restaurant'),
        ),
    ]
