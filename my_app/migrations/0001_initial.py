# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-11 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.IntegerField()),
                ('b', models.IntegerField()),
                ('date', models.DateTimeField(verbose_name='date created')),
            ],
        ),
    ]