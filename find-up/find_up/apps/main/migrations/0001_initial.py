# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import find_up.apps.main.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=40)),
                ('descripcion', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ciudad', models.CharField(max_length=200)),
                ('barrio', models.CharField(max_length=200)),
                ('calle_pricipal', models.CharField(max_length=200)),
                ('calle_secundaria', models.CharField(max_length=200)),
                ('latitud', models.DecimalField(max_digits=6, decimal_places=2)),
                ('longitud', models.DecimalField(max_digits=6, decimal_places=2)),
                ('referencia', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('horario', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=200)),
                ('precio', models.DecimalField(max_digits=6, decimal_places=2)),
                ('stock', models.IntegerField(default=b'0')),
                ('imagen', models.ImageField(null=True, upload_to=find_up.apps.main.models.url, blank=True)),
                ('categorias', models.ManyToManyField(to='main.Categoria')),
                ('fk_empresa', models.ForeignKey(to='main.Empresa')),
                ('fk_propietario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
