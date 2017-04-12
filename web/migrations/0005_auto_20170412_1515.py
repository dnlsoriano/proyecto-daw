# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20170320_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='local',
            name='categoria',
            field=models.CharField(choices=[('fuente', 'Fuente'), ('parque', 'Parque'), ('museo', 'Museo'), ('teatroAuditorio', 'teatroAuditorio'), ('puerta', 'Puerta'), ('otros', 'Otros')], default='otros', max_length=1),
        ),
        migrations.AddField(
            model_name='turismo',
            name='categoria',
            field=models.CharField(choices=[('copas', 'Copas'), ('noche', 'Noche'), ('comer', 'Comer'), ('tapeo', 'Tapas'), ('dulce', 'Dulce'), ('varios', 'Varios')], default='varios', max_length=1),
        ),
    ]
