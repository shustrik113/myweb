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
    url(r'profile_current_user/$', 'userprofile.views.user_profile'),
    url(r'user/([a-zA-Z0-9]+)/$', 'userprofile.views.some_user_profile'),

    # user
    url(r'loginpage/$', 'userprofile.views.loginPage'),
    url(r'forgotpass/$', 'userprofile.views.forgotPass'),
    url(r'auth/login/$', 'userprofile.views.login'),
    url(r'auth/logout/$', 'userprofile.views.logout'),
    url(r'auth/register/$', 'userprofile.views.register'),
]
