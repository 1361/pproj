# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20180606_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.OneToOneField(to='polls.Products'),
        ),
    ]
