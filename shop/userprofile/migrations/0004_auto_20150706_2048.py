# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20150706_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='ava',
            field=models.ImageField(upload_to=b'static/images/avatars/', null=True, verbose_name=b'\xd0\x90\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb0\xd1\x80', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(null=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x80\xd0\xbe\xd0\xb6\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.CharField(max_length=50, verbose_name=b'\xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xbc\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x8f', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='likes_cheese',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\x9b\xd1\x8e\xd0\xb1\xd0\xb8\xd1\x82 \xd1\x81\xd1\x8b\xd1\x80'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.BooleanField(default=True, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb'),
        ),
    ]
