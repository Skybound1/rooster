# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-13 10:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0003_auto_20160202_1243'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='scheduleentry',
            managers=[
                ('entries', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='scheduleentry',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule', to='scheduler.Event'),
        ),
    ]