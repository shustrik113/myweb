# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20150705_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='num_comments',
            field=models.IntegerField(default=0),
        ),
    ]
