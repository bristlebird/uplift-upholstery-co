# Generated by Django 3.2.25 on 2025-03-14 22:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_quantity_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity_available',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
