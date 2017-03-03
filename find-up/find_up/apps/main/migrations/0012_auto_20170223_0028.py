# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20170223_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfiles',
            name='cedula',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perfiles',
            name='movil',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
