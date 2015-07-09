# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_auto_20150707_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='num_pub',
            field=models.IntegerField(default=0),
        ),
    ]
