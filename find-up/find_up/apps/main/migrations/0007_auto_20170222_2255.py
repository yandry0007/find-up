# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import find_up.apps.main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20170126_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfiles',
            name='cedula',
            field=models.IntegerField(unique=True, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perfiles',
            name='correo',
            field=models.EmailField(unique=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='perfiles',
            name='foto',
            field=models.ImageField(null=True, upload_to=find_up.apps.main.models.url3, blank=True),
        ),
        migrations.AlterField(
            model_name='perfiles',
            name='movil',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='perfiles',
            name='telefono',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
