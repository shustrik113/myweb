# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import book.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('other', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=40)),
                ('biography', models.TextField()),
                ('email', models.EmailField(max_length=254, verbose_name=b'e-mail', blank=True)),
                ('slug', models.SlugField(default=book.models.default_slug, unique=True)),
            ],
            options={
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(default=book.models.default_slug, unique=True)),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('price', models.DecimalField(max_digits=1000, decimal_places=2)),
                ('date', models.DateTimeField()),
                ('likes', models.IntegerField(default=0)),
                ('image', models.ImageField(null=True, upload_to=b'static/images/books/', blank=True)),
                ('authors', models.ManyToManyField(to='book.Author')),
                ('cath', models.ForeignKey(to='other.Category')),
                ('langs', models.ManyToManyField(to='other.Lang')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50, blank=True)),
                ('city', models.CharField(max_length=60, verbose_name=b'\xd0\x93\xd0\xbe\xd1\x80\xd0\xbe\xd0\xb4')),
                ('state_province', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=50, verbose_name=b'\xd0\xa1\xd1\x82\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb0')),
                ('website', models.URLField()),
                ('slug', models.SlugField(default=book.models.default_slug, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(to='book.Publisher'),
        ),
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(to='other.Tag'),
        ),
        migrations.AddField(
            model_name='book',
            name='unit',
            field=models.ForeignKey(to='other.Unit'),
        ),
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.ForeignKey(verbose_name='\u0410\u0432\u0442\u043e\u0440', to=settings.AUTH_USER_MODEL),
        ),
    ]
