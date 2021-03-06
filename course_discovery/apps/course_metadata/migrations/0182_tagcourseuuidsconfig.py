# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-14 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0181_auto_20190613_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagCourseUuidsConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.TextField(default=None, null=True, verbose_name='Tag')),
                ('course_uuids', models.TextField(default=None, null=True, verbose_name='Course UUIDs')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
