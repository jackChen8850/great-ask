# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-30 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_auto_20171030_2359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='choice_box',
        ),
        migrations.AddField(
            model_name='choicebox',
            name='choices',
            field=models.ManyToManyField(to='survey.Choice', verbose_name='选项'),
        ),
    ]
