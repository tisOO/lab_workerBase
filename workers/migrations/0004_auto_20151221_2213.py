# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-21 19:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0003_auto_20151221_2213'),
        ('workers', '0003_auto_20151221_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobposition',
            name='position_id',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='department.DepartmentJobPosition', verbose_name='Должность на нашем предприятии'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobposition',
            name='position',
            field=models.CharField(blank=True, max_length=128, verbose_name='Должность/особое название должности'),
        ),
    ]
