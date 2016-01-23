# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-23 14:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
                ('slots_per_day', models.PositiveSmallIntegerField()),
                ('number_of_days', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.Event')),
            ],
        ),
        migrations.CreateModel(
            name='JobResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(blank=True, null=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='scheduler.Job')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('type', models.CharField(choices=[('integer', 'Integer'), ('bool', 'True/False')], default='integer', max_length=20)),
                ('visible', models.BooleanField(default=True)),
                ('default_value', models.IntegerField(default=0)),
                ('min_value', models.IntegerField(blank=True, default=0, null=True)),
                ('max_value', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('real_name', models.CharField(max_length=200)),
                ('email_address', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('public_name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.Event')),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(blank=True, null=True)),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.Resource')),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='scheduler.Volunteer')),
            ],
        ),
        migrations.AddField(
            model_name='jobresource',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.Resource'),
        ),
    ]
