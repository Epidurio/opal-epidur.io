# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-20 11:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('epidurio', '0016_auto_20180220_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consent',
            name='complications',
        ),
        migrations.RemoveField(
            model_name='consent',
            name='number_of_attempts',
        ),
        migrations.RemoveField(
            model_name='consent',
            name='outcome',
        ),
    ]