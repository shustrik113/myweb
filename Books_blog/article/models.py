#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib import admin
# from django.contrib.auth.models import User
# import datetime
# import random


class Article(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    date = models.DateTimeField()
    likes = models.IntegerField(default=0)
    image = models.ImageField()
    image = models.ImageField(upload_to="static/images/articles/", blank=True, null=True)
    num_comments = models.IntegerField(default=0)

    class Meta():
        db_table = "article"


class Comment(models.Model):
    title = models.CharField(max_length=100, default="no title", verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст комментария")
    date = models.DateTimeField()
    likes = models.IntegerField(default=0)
    article = models.ForeignKey(Article)

    class Meta():
        db_table = "comment"


class Game(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    date = models.DateTimeField()
    likes = models.IntegerField(default=0)
    image = models.ImageField()

    class Meta():
        db_table = "game"


class GameComment(models.Model):
    title = models.CharField(max_length=100, default="no title", verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст комментария")
    date = models.DateTimeField()
    likes = models.IntegerField(default=0)
    article = models.ForeignKey(Game)

    class Meta():
        db_table = "game_comment"


# --------------------ADMINKO--------------------------------


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'date')
    list_filter = ['date', 'title', 'likes']
    search_fields = ('title', 'text', 'date')
    fields = ['title', 'text', 'date', 'image']


class GameInline(admin.StackedInline):
    model = GameComment
    extra = 2


class GameAdmin(admin.ModelAdmin):
    fields = ['title', 'text', 'date']
    inlines = [GameInline]
    list_filter = ['date']


admin.site.register(Game, GameAdmin)
admin.site.register(Article, ArticleAdmin)