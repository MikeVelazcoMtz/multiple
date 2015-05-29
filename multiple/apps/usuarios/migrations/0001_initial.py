# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.usuarios.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre', models.CharField(max_length=50, verbose_name=b'Nombre')),
                ('Foto', models.ImageField(upload_to=apps.usuarios.models.content_file_name)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
            bases=(models.Model,),
        ),
    ]
