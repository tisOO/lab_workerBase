# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-17 03:26
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('honors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AchievementReadOnlyProxy',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('honors.achievement',),
        ),
        migrations.CreateModel(
            name='PrizeReadOnlyProxy',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('honors.prize',),
        ),
        migrations.CreateModel(
            name='SalaryReadOnlyProxy',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('honors.salary',),
        ),
        migrations.AddField(
            model_name='achievement',
            name='worker',
            field=models.ForeignKey(default=datetime.datetime(2015, 12, 17, 3, 26, 58, 270579, tzinfo=utc), on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
