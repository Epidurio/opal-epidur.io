# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-21 23:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('epidurio', '0026_auto_20180221_2314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='epiduralinsertion',
            name='procedure_fk',
        ),
        migrations.RemoveField(
            model_name='epiduralinsertion',
            name='procedure_ft',
        ),
    ]
