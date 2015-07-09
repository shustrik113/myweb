# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0007_userprofile_is_priv_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(default=b'Neutrum', max_length=10, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb', choices=[(b'Male', b'Male'), (b'Female', b'Female'), (b'Neutrum', b'Neutrum')]),
        ),
    ]
