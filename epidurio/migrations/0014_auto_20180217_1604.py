# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-17 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epidurio', '0013_asepsis'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asepsis',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='asepsis',
            name='episode',
        ),
        migrations.RemoveField(
            model_name='asepsis',
            name='updated_by',
        ),
        migrations.AddField(
            model_name='epiduralinsertion',
            name='chlorhex',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='epiduralinsertion',
            name='drape',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='epiduralinsertion',
            name='gloves',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='epiduralinsertion',
            name='gown',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='epiduralinsertion',
            name='hat',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='epiduralinsertion',
            name='mask',
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name='Asepsis',
        ),
    ]