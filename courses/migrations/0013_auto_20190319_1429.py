# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-19 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_auto_20190315_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_max_students',
            field=models.IntegerField(default=200),
        ),
    ]