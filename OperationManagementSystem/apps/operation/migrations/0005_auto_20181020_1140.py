# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-20 03:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0004_auto_20181018_1005'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SLBToSite',
            new_name='SLBToApplication',
        ),
    ]
