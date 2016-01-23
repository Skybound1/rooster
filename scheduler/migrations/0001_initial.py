# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-23 11:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Constraint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('integer_value', models.IntegerField(null=True)),
                ('boolean_value', models.NullBooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ConstraintDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('data_type', models.CharField(choices=[('int', 'Integer'), ('bool', 'True/False')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
                ('day_length', models.PositiveSmallIntegerField()),
                ('day_count', models.PositiveSmallIntegerField()),
                ('job_constraints', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_events', to='scheduler.ConstraintDescription')),
                ('volunteer_constraints', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='volunteer_events', to='scheduler.ConstraintDescription')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('constraints', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.Constraint')),
                ('description', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.ConstraintDescription')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.Event')),
            ],
        ),
        migrations.CreateModel(
            name='JobDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('real_name', models.CharField(max_length=200)),
                ('email_address', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('public_name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('constraints', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.Constraint')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.Event')),
            ],
        ),
        migrations.AddField(
            model_name='constraint',
            name='description',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.ConstraintDescription'),
        ),
    ]
