# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-15 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_trippreference_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='flightpreference',
            name='alliance',
            field=models.CharField(choices=[('*A', 'Star Alliance'), ('*O', 'One World'), ('*S', 'Sky Team')], max_length=100),
        ),
    ]