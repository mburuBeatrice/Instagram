# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-08 05:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaclone', '0009_auto_20180308_0810'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['user']},
        ),
        migrations.AlterField(
            model_name='post',
            name='comment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]