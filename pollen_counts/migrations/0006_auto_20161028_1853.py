# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 18:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollen_counts', '0005_auto_20161028_1853'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pollencounts',
            old_name='total',
            new_name='total_grass',
        ),
    ]
