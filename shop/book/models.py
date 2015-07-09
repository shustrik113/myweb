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


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    biography = models.TextField()
    email = models.EmailField('e-mail', blank=True)
    slug = models.SlugField(unique=True, default = default_slug)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    class Meta:
        ordering = ['last_name']


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50, blank=True)
    city = models.CharField("Город", max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField("Страна", max_length=50)
    website = models.URLField()
    slug = models.SlugField(unique=True, default = default_slug)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Book(models.Model):
    slug = models.SlugField(unique=True, default=default_slug)
    unit = models.ForeignKey(Unit)
    cath = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag)
    langs = models.ManyToManyField(Lang)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    user = models.ForeignKey(User, verbose_name=u'Автор')
    num_comments = models.IntegerField(default=0)
    title = models.CharField(max_length=80)
    text = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    image = models.ImageField(upload_to="static/images/books/", blank=True, null=True)
    item_type = models.CharField(max_length=50, default="book")

    class Meta:
        ordering = ['date']

    def __unicode__(self):
        return self.title + u' (' + self.unit.name + u')'

    def get_absolute_url(self):
        return "/books/book/%s" % self.slug


class CommentBook(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(verbose_name='Текст комментария:')
    user = models.ForeignKey(User, verbose_name=u'Автор')
    book = models.ForeignKey(Book)
    likes = models.IntegerField(default=0)

    class Meta:
        db_table = 'comment_book'


# --------------------ADMINKO--------------------------------


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'publisher', 'image', 'cath', 'likes', 'date')
    list_filter = ['date', 'title', 'likes', 'authors', 'publisher', 'cath']
    search_fields = ('title', 'text', 'date')
    fields = ['title', 'text', 'image', 'slug', 'authors', 'publisher', 'cath', 'tags', 'langs', 'unit', 'price', 'user']


class PublisherAdmin(admin.ModelAdmin):
    search_fields = ('name', 'address', 'city')
    list_filter = ['name', 'city', 'country']


class AuthorAdmin(admin.ModelAdmin):
    list_filter = ['last_name', 'first_name']
    search_fields = ('first_name', 'last_name', 'biography')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)



