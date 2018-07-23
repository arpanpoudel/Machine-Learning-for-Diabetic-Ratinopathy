# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-08 06:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='All_hostel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=200)),
                ('facilities', models.CharField(default='DEFAULT VALUE', max_length=500)),
                ('admission_fee', models.CharField(max_length=200)),
                ('monthly_charge', models.CharField(max_length=200)),
                ('owner', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('deposit', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=200)),
                ('longitude', models.CharField(max_length=200)),
            ],
        ),
    ]
