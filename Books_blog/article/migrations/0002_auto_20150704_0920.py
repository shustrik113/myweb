# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='num_comments',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(null=True, upload_to=b'static/images/articles/', blank=True),
        ),
    ]
