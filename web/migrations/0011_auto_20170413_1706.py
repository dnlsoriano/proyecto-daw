# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-13 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_auto_20170413_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='local',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='local',
            name='telefono',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]