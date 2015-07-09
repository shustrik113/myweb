#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
import datetime
import random


def default_slug():
    Dt = datetime.datetime.now()
    return u's%04d%02d%02d%02d%02d%02d%03d' % (
                       Dt.year, Dt.month, Dt.day, Dt.hour,
                       Dt.minute, Dt.second, random.randint(0, 999))


class Tag(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False, unique=True)
    slug = models.SlugField(unique=True, default=default_slug)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True, default=default_slug)
    items = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = u'Categories'
        ordering = [u'name']


class Lang(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.code + u' -- ' + self.name


class Unit(models.Model):
    name = models.CharField(unique=True, max_length=20)

    def __unicode__(self):
        return self.name


# --------------------------POLL-----------------------------------


class Question(models.Model):
    text = models.CharField(max_length=200)
    date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question)
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


# --------------------MENU--------------------------------


class Menu(models.Model):
    name = models.CharField(max_length=20)
    name_link = models.CharField(max_length=20)
    submenu_cat = models.BooleanField(default=False)

    class Meta:
        db_table = 'menu'


# --------------------ADMINKO--------------------------------


class MenuAdmin(admin.ModelAdmin):
    fields = ['name', 'name_link', 'submenu_cat']
    list_display = ('name', 'name_link', 'submenu_cat')


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', )
    fields = ['name', 'slug']


class LangAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', )


class UnitAdmin(admin.ModelAdmin):
    search_fields = ('name', )


class QuestionInline(admin.TabularInline):  # компактнее, чем StackedInLine
    model = Choice
    extra = 10
    fields = ['text']


class QuestionAdmin(admin.ModelAdmin):
    fields = ['text', 'date']
    inlines = [QuestionInline]
    list_filter = ['date']
    list_display = ('text', 'date')
    search_fields = ['text']


admin.site.register(Menu, MenuAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Lang, LangAdmin)
admin.site.register(Unit, UnitAdmin)