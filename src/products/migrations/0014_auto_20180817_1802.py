# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-08-17 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20180817_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productregister',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/images'),
        ),
    ]
