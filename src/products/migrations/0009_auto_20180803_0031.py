# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-08-03 00:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20180802_2352'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductProvider',
            new_name='ProviderRegister',
        ),
    ]