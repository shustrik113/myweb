# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('other', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num_comments', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=150)),
                ('text', models.TextField()),
                ('date', models.DateTimeField()),
                ('likes', models.IntegerField(default=0)),
                ('image', models.ImageField(null=True, upload_to=b'static/images/articles/', blank=True)),
                ('is_private', models.BooleanField(default=False, verbose_name='\u041f\u0440\u0438\u0432\u0430\u0442\u043d\u0430\u044f \u0441\u0442\u0430\u0442\u044c\u044f?')),
                ('cath', models.ForeignKey(to='other.Category')),
                ('tags', models.ManyToManyField(to='other.Tag')),
                ('user', models.ForeignKey(verbose_name='\u0410\u0432\u0442\u043e\u0440', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['date'],
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('text', models.TextField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82 \xd0\xba\xd0\xbe\xd0\xbc\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x80\xd0\xb8\xd1\x8f:')),
                ('likes', models.IntegerField(default=0)),
                ('article', models.ForeignKey(to='article.Article')),
                ('user', models.ForeignKey(verbose_name='\u0410\u0432\u0442\u043e\u0440', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'comment',
            },
        ),
    ]
