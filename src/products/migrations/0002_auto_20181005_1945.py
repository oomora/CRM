# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-05 19:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productregister',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.CategoryCatalogue'),
        ),
    ]
