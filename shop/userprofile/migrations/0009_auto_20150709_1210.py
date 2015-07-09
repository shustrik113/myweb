# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0008_auto_20150709_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(default='\u041d\u0435\u0438\u0437\u0432\u0435\u0441\u0442\u043d\u043e', max_length=10, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb', choices=[('\u041c\u0443\u0436\u0441\u043a\u043e\u0439', b'Male'), ('\u0416\u0435\u043d\u0441\u043a\u0438\u0439', b'Female'), ('\u041d\u0435\u0438\u0437\u0432\u0435\u0441\u0442\u043d\u043e', b'Neutrum')]),
        ),
    ]
