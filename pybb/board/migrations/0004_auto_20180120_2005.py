# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-20 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='reply_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='topic',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
