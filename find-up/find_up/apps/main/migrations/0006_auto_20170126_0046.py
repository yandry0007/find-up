# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_perfiles'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='direccion',
            options={'verbose_name': 'Direccion', 'verbose_name_plural': 'Direcciones'},
        ),
        migrations.AddField(
            model_name='perfiles',
            name='tipo_registro',
            field=models.CharField(default=b'facebook', max_length=30),
        ),
    ]
