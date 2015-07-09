#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.files.base import ContentFile

from django.shortcuts import render_to_response, redirect
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.contrib import auth
import datetime
import re

from django.core import serializers
import json

from article.models import Article, Comment
from book.models import Book
from models import Category, Tag, Question, Choice, Menu

# from formtools.wizard.views import SessionWizardView
# from django.core.mail import send_mail
# import logging

# logr = logging.getLogger(__name__)


# Starting website
def index(request):
    args = {}
    args.update(csrf(request))
    args['menu'] = Menu.objects.all()
    args['this_page'] = '/'

    # right box
    args['pop_articles'] = Article.objects.all().order_by('likes').reverse()[:10]
    args['new_articles'] = Article.objects.all().order_by('date').reverse()[:10]
    args['cats'] = Category.objects.all()
    args['tags'] = Tag.objects.all()
    args['current_item'] = 'статьи'

    # user
    args['username'] = auth.get_user(request).username

    # poll
    args['question_web'] = Question.objects.get(text=u"Как вам наш сайт?")
    args['choices'] = Choice.objects.filter(question_id=args['question_web'].id)
    return render_to_response('index.html', args)


# Voting polls
def pollVote(request, poll_id=1):
    if request.POST:
        poll = Question.objects.get(id=poll_id)
        radio = request.POST['vote']
        choice = poll.choice_set.get(pk=int(radio))
        choice.votes += 1
        choice.save()

        # poll
        args = {}
        args.update(csrf(request))
        args['question_web'] = Question.objects.get(text=u"Как вам наш сайт?")
        args['choices'] = Choice.objects.filter(question_id=args['question_web'].id).order_by('-votes')
    # return render_to_response('test.html', radio)
    return render_to_response('poll.html', args)


# Other page
def other(request):
    args = {}
    args.update(csrf(request))
    args['menu'] = Menu.objects.all()
    args['this_page'] = '/other/'

    # right box
    args['pop_articles'] = Article.objects.all().order_by('likes').reverse()[:10]
    args['new_articles'] = Article.objects.all().order_by('date').reverse()[:10]
    args['cats'] = Category.objects.all()
    args['tags'] = Tag.objects.all()
    args['current_item'] = 'статьи'

    # user
    args['username'] = auth.get_user(request).username

    # poll
    args['question_web'] = Question.objects.get(text=u"Как вам наш сайт?")
    args['choices'] = Choice.objects.filter(question_id=args['question_web'].id)

    args['user_agent'] = request.META['HTTP_USER_AGENT']
    return render_to_response('other.html', args)


# SEARCH
# Down-dropping div of searched items by AJAX
def search(request):
    if request.POST:
        search_text = request.POST['search_text']
    else:
        search_text = ''

    args = {}
    args.update(csrf(request))
    if search_text != '':
        args['searched'] = Article.objects.filter(title__contains=search_text)
    else:
        args['searched'] = ''
    return render_to_response('search.html', args)


# Page of searched items sorted by date
def search_results(request, page_number=1):
    args = {}
    args.update(csrf(request))
    args['menu'] = Menu.objects.all()

    # right box
    args['pop_articles'] = Article.objects.all().order_by('likes').reverse()[:10]
    args['new_articles'] = Article.objects.all().order_by('date').reverse()[:10]
    args['cats'] = Category.objects.all()
    args['tags'] = Tag.objects.all()
    args['current_item'] = 'статьи'

    # user
    args['username'] = request.user

    # poll
    args['question_web'] = Question.objects.get(text=u"Как вам наш сайт?")
    args['choices'] = Choice.objects.filter(question_id=args['question_web'].id)

    items = []

    if request.POST:
        search_text = request.POST['search']
        # Deleting cookies because of new request:
        # if items in request.COOKIES:
        #     HttpResponse.delete_cookie(items)  # !!!!
    else:
        search_text = ''

    # if items in request.COOKIES:
    # convertion from JSON string to list
    # ...
    #     items += request.COOKIES

    if search_text != '' and items == []:
        articles = Article.objects.filter(title__contains=search_text)
        books = Book.objects.filter(title__contains=search_text)

        items += articles
        items += books
        items.sort(key=lambda item: item.date)
        items = items[::-1]

    current_page = Paginator(items, 5)
    args['items'] = current_page.page(page_number)
    args['page_number'] = page_number
    args['count'] = len(Paginator(items, 5).page_range)

    # Saving items in COOKIES:
    # HttpResponse.set_cookie(items, items)
    return render_to_response('search_results.html', args)


# Contact page
def contact(request):
    # right box
    args = {}
    args.update(csrf(request))
    args['menu'] = Menu.objects.all()
    args['this_page'] = '/contact/'
    args['pop_articles'] = Article.objects.all().order_by('likes').reverse()[:10]
    args['new_articles'] = Article.objects.all().order_by('date').reverse()[:10]
    args['cats'] = Category.objects.all()
    args['tags'] = Tag.objects.all()
    args['current_item'] = 'статьи'

    # user
    args['username'] = auth.get_user(request).username

    # poll
    args['question_web'] = Question.objects.get(text=u"Как вам наш сайт?")
    args['choices'] = Choice.objects.filter(question_id=args['question_web'].id)
    return render_to_response('contact/contact.html', args)


# CONTACT WIZARD
# class ContactWizard(SessionWizardView):
#     template_name = 'contact/contact_form.html'

#     def done(self, form_list, **kwargs):
#         args = {}
#         args['form_data'] = process_form_data(form_list)
#         args['menu'] = Menu.objects.all()
#         args['this_page'] = '/contact/'
#         args['pop_articles'] = Article.objects.all().order_by('likes').reverse()[:10]
#         args['new_articles'] = Article.objects.all().order_by('date').reverse()[:10]
#         args['cats'] = Category.objects.all()
#         args['tags'] = Tag.objects.all()
#         args['current_item'] = 'статьи'

#         # poll
#         args['question_web'] = Question.objects.get(text=u"Как вам наш сайт?")
#         args['choices'] = Choice.objects.filter(question_id=args['question_web'].id)
#         return render_to_response('/contact/done.html', args)


# def process_form_data(form_list):
#     form_data = [form.cleaned_data for form in form_list]
#     logr.debug(form_data[0]['subject'])
#     logr.debug(form_data[1]['sender'])
#     logr.debug(form_data[2]['message'])

#     send_mail(form_data[0]['subject'],
#         form_data[2]['message'],
#         form_data[1]['sender'],
#         ['elimoon@mail.ru'], fail_silently=False)
#     return form_data


def test(request):
    args = {}
    args['referer'] = request.META.get('HTTP_REFERER')
    args['path'] = request.path
    args['host'] = request.get_host()
    args['full_path'] = request.get_full_path()

    articles = Article.objects.all()
    books = Book.objects.all()
    items = []

    items += articles
    items += books

    # for book in books:
    #    items.append(book)
    # for article in articles:
    #    items.append(article)

    # items.sort(key=lambda item: item.date)
    # items = items[::-1]

    args['test'] = items
    args['test2'] = articles
    return render_to_response('test.html', args)


