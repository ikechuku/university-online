# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-15 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_auto_20190315_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='professor',
            field=models.CharField(default='Prof Jane Doe', max_length=50),
        ),
    ]
