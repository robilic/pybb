# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-28 18:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0007_auto_20180128_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='created',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='forum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Forum'),
        ),
    ]
