# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0006_userprofile_num_pub'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_priv_email',
            field=models.BooleanField(default=False),
        ),
    ]
