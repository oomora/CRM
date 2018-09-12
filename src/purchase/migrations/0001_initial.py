# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-09-01 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quoteNumber', models.IntegerField(default=0)),
                ('creationDate', models.DateField()),
                ('row', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('unity', models.CharField(default='Pieza', max_length=12)),
                ('description', models.CharField(default='Descripcion del articulo', max_length=30)),
                ('deliveryDate', models.DateField()),
                ('weight', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('rowTotal', models.IntegerField(default=0)),
                ('taxIVA', models.IntegerField(default=16)),
                ('quoteTotal', models.IntegerField(default=0)),
                ('creator', models.CharField(default='OMP', max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Quotes',
            },
        ),
    ]
