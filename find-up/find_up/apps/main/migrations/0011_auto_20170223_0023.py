# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20170222_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfiles',
            name='movil',
            field=models.CharField(default=b'999', max_length=10, null=True, blank=True),
        ),
    ]
