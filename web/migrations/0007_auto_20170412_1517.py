# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20170412_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='local',
            name='categoria',
            field=models.CharField(choices=[('copas', 'Copas'), ('noche', 'Noche'), ('comer', 'Comer'), ('tapeo', 'Tapas'), ('dulce', 'Dulce'), ('varios', 'Varios')], default='varios', max_length=10),
        ),
        migrations.AlterField(
            model_name='turismo',
            name='categoria',
            field=models.CharField(choices=[('fuente', 'Fuente'), ('parque', 'Parque'), ('museo', 'Museo'), ('teatroAuditorio', 'teatroAuditorio'), ('puerta', 'Puerta'), ('otros', 'Otros')], default='otros', max_length=15),
        ),
    ]
