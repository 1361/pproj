# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='unit',
            field=models.CharField(default='', max_length=50),
        ),
    ]
