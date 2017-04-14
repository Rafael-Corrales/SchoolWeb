# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-02 07:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='media/message'),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='leido',
            field=models.BooleanField(default=True),
        ),
    ]