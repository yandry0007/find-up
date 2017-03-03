# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20170222_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfiles',
            name='cedula',
            field=models.IntegerField(default=9999999999, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perfiles',
            name='movil',
            field=models.IntegerField(default=9999999999, null=True, blank=True),
        ),
    ]
