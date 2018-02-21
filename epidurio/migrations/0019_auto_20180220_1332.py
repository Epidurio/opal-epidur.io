# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-20 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epidurio', '0018_technique'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technique',
            name='level',
            field=models.CharField(blank=True, choices=[('L2/3', 'L2/3'), ('L3/4', 'L3/4'), ('L4/5', 'L4/5'), ('Other', 'Other')], max_length=255, null=True),
        ),
    ]
