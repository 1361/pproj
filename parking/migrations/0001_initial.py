# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Citation',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('street', models.CharField(max_length=15)),
                ('date', models.DateTimeField()),
                ('officer', models.CharField(max_length=15)),
            ],
        ),
    ]
