# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollen_counts', '0007_auto_20161028_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pollencounts',
            name='date',
        ),
        migrations.RemoveField(
            model_name='pollencounts',
            name='time',
        ),
        migrations.AddField(
            model_name='pollencounts',
            name='datetime',
            field=models.DateTimeField(null=True),
        ),
    ]
