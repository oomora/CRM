# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-08-15 00:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_ordercatalogue'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryCatalogue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('categoryNumber', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='productregister',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
    ]