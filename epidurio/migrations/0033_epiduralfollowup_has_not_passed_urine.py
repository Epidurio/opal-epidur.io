# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-25 10:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epidurio', '0032_auto_20180225_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='epiduralfollowup',
            name='has_not_passed_urine',
            field=models.BooleanField(default=False),
        ),
    ]
