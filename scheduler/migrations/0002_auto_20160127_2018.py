# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-27 20:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManualScheduleEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField()),
                ('time_slot', models.IntegerField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.Event')),
            ],
        ),
        migrations.RemoveField(
            model_name='jobresource',
            name='value',
        ),
        migrations.AddField(
            model_name='jobresource',
            name='min_value',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobresource',
            name='target_value',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='scheduler.Event'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='type',
            field=models.CharField(choices=[('integer', 'Integer'), ('boolean', 'True/False')], default='integer', max_length=20),
        ),
        migrations.AddField(
            model_name='manualscheduleentry',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='scheduler.Job'),
        ),
        migrations.AddField(
            model_name='manualscheduleentry',
            name='volunteer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='scheduler.Volunteer'),
        ),
    ]
