# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-14 04:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faith_pms', '0006_doctor_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='faith_pms.Doctor'),
        ),
    ]
