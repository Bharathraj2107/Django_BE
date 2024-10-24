# Generated by Django 4.0.3 on 2024-10-24 11:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lib_customers',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]