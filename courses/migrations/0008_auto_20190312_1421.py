# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-12 13:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20190312_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='profile_pic',
            field=models.ImageField(upload_to=''),
        ),
    ]
