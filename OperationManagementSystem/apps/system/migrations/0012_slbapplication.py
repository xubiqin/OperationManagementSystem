# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-20 08:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0011_auto_20181020_0909'),
    ]

    operations = [
        migrations.CreateModel(
            name='SLBApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SLB', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.SLB', verbose_name='\u6240\u5c5eSLB')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Application', verbose_name='\u6240\u5c5e\u5e94\u7528')),
            ],
            options={
                'verbose_name': 'SLB\u4e0e\u5e94\u7528\u7684\u5173\u8054\u5173\u7cfb',
                'verbose_name_plural': 'SLB\u4e0e\u5e94\u7528\u7684\u5173\u8054\u5173\u7cfb',
            },
        ),
    ]
