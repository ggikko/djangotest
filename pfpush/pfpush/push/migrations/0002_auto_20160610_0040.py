# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-10 00:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('push', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, default='', max_length=10)),
                ('token', models.CharField(blank=True, default='', max_length=100)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.AlterModelOptions(
            name='push',
            options={'ordering': ('sendtime',)},
        ),
        migrations.RenameField(
            model_name='push',
            old_name='created',
            new_name='sendtime',
        ),
        migrations.RemoveField(
            model_name='push',
            name='token',
        ),
        migrations.AddField(
            model_name='push',
            name='target',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='push',
            name='title',
            field=models.TextField(),
        ),
    ]
