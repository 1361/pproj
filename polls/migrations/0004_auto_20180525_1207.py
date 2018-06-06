# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_producerprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producerprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='ProducerProfile',
        ),
    ]
