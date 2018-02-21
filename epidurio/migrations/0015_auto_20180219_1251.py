# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-19 12:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opal', '0034_auto_20171214_1845'),
        ('epidurio', '0014_auto_20180217_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asepsis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('gloves', models.BooleanField(default=True)),
                ('gown', models.BooleanField(default=True)),
                ('hat', models.BooleanField(default=True)),
                ('mask', models.BooleanField(default=True)),
                ('drape', models.BooleanField(default=True)),
                ('chlorhex', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_epidurio_asepsis_subrecords', to=settings.AUTH_USER_MODEL)),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_epidurio_asepsis_subrecords', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.RemoveField(
            model_name='epiduralinsertion',
            name='chlorhex',
        ),
        migrations.RemoveField(
            model_name='epiduralinsertion',
            name='drape',
        ),
        migrations.RemoveField(
            model_name='epiduralinsertion',
            name='gloves',
        ),
        migrations.RemoveField(
            model_name='epiduralinsertion',
            name='gown',
        ),
        migrations.RemoveField(
            model_name='epiduralinsertion',
            name='hat',
        ),
        migrations.RemoveField(
            model_name='epiduralinsertion',
            name='mask',
        ),
    ]
