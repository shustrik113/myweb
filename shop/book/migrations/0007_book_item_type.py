# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_auto_20150706_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='item_type',
            field=models.CharField(default=b'book', max_length=50),
        ),
    ]
