# Generated by Django 5.0.4 on 2025-01-12 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('category', models.CharField(max_length=50)),
                ('latitude', models.DecimalField(blank=True, decimal_places=11, max_digits=21, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=11, max_digits=21, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'restaurants',
            },
        ),
    ]
