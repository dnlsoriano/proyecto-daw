# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20170412_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turismo',
            name='categoria',
            field=models.CharField(choices=[('fuente', 'Fuente'), ('parque', 'Parque'), ('museo', 'Museo'), ('teatro', 'Teatro'), ('auditorio', 'Auditorio'), ('puerta', 'Puerta'), ('otros', 'Otros')], default='otros', max_length=15),
        ),
    ]
