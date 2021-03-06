# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-05 20:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20181005_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorycatalogue',
            name='id',
        ),
        migrations.AlterField(
            model_name='categorycatalogue',
            name='category_number',
            field=models.CharField(max_length=5, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productregister',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.CategoryCatalogue'),
        ),
    ]
