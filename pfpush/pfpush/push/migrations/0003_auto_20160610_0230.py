# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-10 02:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('push', '0002_auto_20160610_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
    ]
