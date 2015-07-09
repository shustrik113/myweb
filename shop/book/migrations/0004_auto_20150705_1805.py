# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_commentbook'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentbook',
            old_name='article',
            new_name='book',
        ),
    ]
