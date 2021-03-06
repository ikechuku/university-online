# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-19 13:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=300)),
                ('gender', models.CharField(max_length=10)),
                ('profile_pic', models.FileField(upload_to='Professors')),
                ('mobile_no', models.CharField(blank=True, max_length=30)),
                ('address', models.TextField(blank=True, max_length=100)),
                ('education', models.TextField(blank=True, max_length=130)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
