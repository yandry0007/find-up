# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_empresa_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='direccion',
            name='fk_empresa',
        ),
        migrations.AddField(
            model_name='empresa',
            name='fk_direccion',
            field=models.ForeignKey(blank=True, to='main.Direccion', null=True),
        ),
    ]
