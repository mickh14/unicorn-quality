# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-26 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0020_auto_20200320_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(blank=True, choices=[('ToDo', 'ToDo'), ('InDevelopment', 'InDevelopment'), ('ReadyForTest', 'ReadyForTest')], max_length=30),
        ),
        migrations.AlterField(
            model_name='issue',
            name='votes',
            field=models.IntegerField(default='1'),
        ),
    ]