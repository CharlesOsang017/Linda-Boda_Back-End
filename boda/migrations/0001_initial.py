# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-11-05 11:22
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('city_destination', models.CharField(max_length=60)),
                ('county', models.CharField(max_length=35)),
                ('phone_number', models.DecimalField(decimal_places=2, max_digits=20)),
                ('country', django_countries.fields.CountryField(default='KE', max_length=2)),
            ],
            options={
                'verbose_name': 'Passenger',
                'verbose_name_plural': 'Passengers',
            },
        ),
    ]
