# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-05 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0007_auto_20200305_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='actual_Results',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='issue',
            name='expected_Results',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='issue',
            name='step_to_Reproduce',
            field=models.CharField(default='', max_length=1000),
        ),
    ]