#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Books_blog URL Configuration

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
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'article.views.index'),
    url(r'^article/([a-zA-Z0-9]+)/$', 'article.views.article'),
    url(r'^article/addlike/([a-zA-Z0-9]+)/$', 'article.views.addlike'),
    url(r'^article/addcomment/([a-zA-Z0-9]+)/$', 'article.views.addcomment'),

    url(r'^games/$', 'article.views.games'),
    url(r'^game/([a-zA-Z0-9]+)/$', 'article.views.game'),
    # url(r'^game/addlike/([a-zA-Z0-9]+)/$', 'article.views.game_addlike'),
    # url(r'^game/addcomment/([a-zA-Z0-9]+)/$', 'article.views.game_addcomment'),
]
