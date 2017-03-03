# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20170222_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfiles',
            name='movil',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perfiles',
            name='tipo_registro',
            field=models.CharField(default=b'facebook', max_length=30, null=True, blank=True),
        ),
    ]
