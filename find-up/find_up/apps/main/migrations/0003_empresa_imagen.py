# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import find_up.apps.main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_direccion_fk_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='imagen',
            field=models.ImageField(null=True, upload_to=find_up.apps.main.models.url2, blank=True),
        ),
    ]
