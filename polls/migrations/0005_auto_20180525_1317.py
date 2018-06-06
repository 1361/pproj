# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20180525_1207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('listing_name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=200)),
                ('amount_available', models.IntegerField(default=0)),
                ('list_price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('listing', models.ForeignKey(to='polls.Listing')),
            ],
        ),
        migrations.DeleteModel(
            name='Car',
        ),
    ]
