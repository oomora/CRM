# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-08-02 17:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_contactregister'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactregister',
            old_name='mail',
            new_name='email',
        ),
    ]