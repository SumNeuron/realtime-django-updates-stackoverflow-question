# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-11 08:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myquery',
            name='total',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]
