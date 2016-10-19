# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-19 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0010_auto_20160914_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='scan',
            name='curl_http',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scan',
            name='curl_http_www',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scan',
            name='curl_https',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scan',
            name='curl_https_www',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scan',
            name='pshtt_stderr',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scan',
            name='pshtt_stdout',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
