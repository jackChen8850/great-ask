# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-01 11:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0008_auto_20171101_1012'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeetingRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addr', models.CharField(max_length=32, verbose_name='会议室地点')),
            ],
        ),
        migrations.CreateModel(
            name='MeetingRoomBookList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='开始时间')),
                ('end_time', models.DateTimeField(verbose_name='结束时间')),
                ('for_who', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.UserInfo', verbose_name='为谁预定')),
                ('meeting_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.MeetingRoom', verbose_name='会议室')),
            ],
        ),
        migrations.CreateModel(
            name='SurveyItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='问题')),
                ('type', models.SmallIntegerField(choices=[(1, '单选'), (2, '多选'), (3, '打分题'), (4, 'text'), (5, 'text-area')], default=1, verbose_name='类型')),
            ],
        ),
        migrations.RemoveField(
            model_name='choicebox',
            name='choices',
        ),
        migrations.RemoveField(
            model_name='choicerecord',
            name='survey',
        ),
        migrations.RemoveField(
            model_name='inputrecord',
            name='survey',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='choice_boxes',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='input_boxes',
        ),
        migrations.AlterField(
            model_name='choicerecord',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Choice', verbose_name='答案'),
        ),
        migrations.AlterField(
            model_name='choicerecord',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.SurveyItem', verbose_name='问题'),
        ),
        migrations.AlterField(
            model_name='inputrecord',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.SurveyItem', verbose_name='问题'),
        ),
        migrations.DeleteModel(
            name='ChoiceBox',
        ),
        migrations.DeleteModel(
            name='InputBox',
        ),
        migrations.AddField(
            model_name='choice',
            name='survey_item',
            field=models.ManyToManyField(to='survey.SurveyItem', verbose_name='所属题目'),
        ),
    ]
