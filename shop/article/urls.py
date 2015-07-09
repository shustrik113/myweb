#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # articles
    url(r'article/([a-zA-Z0-9]+)/page/([0-9]+)/$', 'article.views.article', name="article_page_comments"),

    url(r'page/(?P<page_number>[0-9]+)/$', 'article.views.articles', name="article_page"),
    url(r'cat/(?P<cat_slug>[a-zA-Z0-9]+)/page/(?P<page_number>[0-9]+)$', 'article.views.articles_cat', name="article_page_category"),
    url(r'cat/(?P<cat_slug>[a-zA-Z0-9]+)/$', 'article.views.articles_cat', name="article_category"),
    url(r'tag/([a-zA-Z0-9]+)/$', 'article.views.tag', name="tag"),

    url(r'article/([0-9]+)/$', 'article.views.article', name="article"),
    url(r'article/addlike/$', 'article.views.addlike', name="article_addlike"),
    url(r'article/addcomment/([a-zA-Z0-9]+)/$', 'article.views.addcomment', name="article_addcomment"),

    url(r'newarticle/$', 'article.views.newArticle', name="new_article"),
    url(r'savearticle/$', 'article.views.saveArticle', name="save_article"),

    # comments
    url(r'comment/addlike/([a-zA-Z0-9]+)/$', 'article.views.addlike_Comment', name="comment_addlike"),

    url(r'^$', 'article.views.articles', name="articles"),

]
