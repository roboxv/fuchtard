# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20160529_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='url',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Ссылка'),
            preserve_default=False,
        ),
    ]
