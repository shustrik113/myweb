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

# from forms import ContactForm1, ContactForm2, ContactForm3
# from views import ContactWizard


urlpatterns = [
    url(r'poll/vote/([0-9]+)/$', 'other.views.pollVote', name="poll"),
    url(r'search/$', 'other.views.search'),
    url(r'search_results/$', 'other.views.search_results'),
    url(r'search_results/page/([0-9]+)/$', 'other.views.search_results'),

    # contact
    # url(r'feedback/$', ContactWizard.as_view([ContactForm1, ContactForm2, ContactForm3])),

    url(r'test/$', 'other.views.test'),

    url(r'^$', 'other.views.other', name="other"),
]
