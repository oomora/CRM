# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-08-04 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20180803_0031'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderCatalogue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('label', models.CharField(max_length=20)),
            ],
        ),
    ]