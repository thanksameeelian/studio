# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-01-30 23:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contentcuration', '0078_auto_20171024_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentnode',
            name='publishing',
            field=models.BooleanField(default=False),
        ),
    ]