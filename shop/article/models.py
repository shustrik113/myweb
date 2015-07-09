#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
import datetime
import random

from other.models import Tag, Category, Lang, Unit


def default_slug():
    Dt = datetime.datetime.now()
    return u's%04d%02d%02d%02d%02d%02d%03d' % (
                       Dt.year, Dt.month, Dt.day, Dt.hour,
                       Dt.minute, Dt.second, random.randint(0, 999))


class Article(models.Model):
    num_comments = models.IntegerField(default=0)
    cath = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag)
    title = models.CharField(max_length=150)
    text = models.TextField()
    date = models.DateTimeField()
    likes = models.IntegerField(default=0)
    image = models.ImageField(upload_to="static/images/articles/", blank=True, null=True)
    item_type = models.CharField(max_length=50, default="article")

    is_private = models.BooleanField(default=False, verbose_name=u'Приватная статья?')
    user = models.ForeignKey(User, verbose_name=u'Автор')

    class Meta:
        ordering = ['date']
        db_table = 'article'

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    date = models.DateTimeField()
    text = models.TextField(verbose_name='Текст комментария:')
    user = models.ForeignKey(User, verbose_name=u'Автор')
    article = models.ForeignKey(Article)
    likes = models.IntegerField(default=0)

    class Meta:
        db_table = 'comment'


# --------------------ADMINKO--------------------------------


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'date', 'is_private', 'user')
    list_filter = ['date', 'title', 'likes', 'is_private', 'cath', 'tags', 'user']
    search_fields = ('title', 'text', 'date', 'user')
    fields = ['title', 'text', 'date', 'image', 'is_private', 'cath', 'tags', 'user']


admin.site.register(Article, ArticleAdmin)



