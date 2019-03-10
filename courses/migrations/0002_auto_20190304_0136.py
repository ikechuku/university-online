# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-04 00:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_duration',
            field=models.CharField(default='3 months', max_length=30),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=30),
        ),
    ]