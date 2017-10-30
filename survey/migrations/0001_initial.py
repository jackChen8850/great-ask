# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-30 12:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rbac', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='选项名称')),
                ('is_checked', models.BooleanField(default=False, verbose_name='是否选中')),
            ],
        ),
        migrations.CreateModel(
            name='ChoiceBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='问题名称')),
                ('type', models.SmallIntegerField(choices=[(1, '单选'), (2, '多选')], default=1, verbose_name='选项类型')),
            ],
        ),
        migrations.CreateModel(
            name='InputBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='问题名称')),
                ('answer', models.CharField(blank=True, max_length=200, null=True, verbose_name='答案')),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_created=True, verbose_name='创建日期')),
                ('title', models.CharField(max_length=128, verbose_name='问卷名称')),
            ],
        ),
        migrations.CreateModel(
            name='TextArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='问题名称')),
                ('answer', models.TextField(blank=True, max_length=200, null=True, verbose_name='答案')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Survey', verbose_name='所属问卷')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rbac.User', verbose_name='用户账号')),
            ],
        ),
        migrations.AddField(
            model_name='inputbox',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Survey', verbose_name='所属问卷'),
        ),
        migrations.AddField(
            model_name='choicebox',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Survey', verbose_name='所属问卷'),
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_box',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.ChoiceBox', verbose_name='所属问题'),
        ),
    ]
