#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.files.base import ContentFile

from django.shortcuts import render_to_response, redirect
from django.http import Http404, HttpResponseRedirect
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.contrib import auth
import datetime
import re

# from models import Game
from other.models import Category, Tag, Unit, Question, Choice, Menu
from book.models import Book

# GAMES
def games(request, page_number=1):
    # right box
    args = {}
    args.update(csrf(request))
    args['menu'] = Menu.objects.all()
    args['this_page'] = '/games/'
    args['pop_games'] = Book.objects.all().order_by('likes').reverse()[:10]
    args['new_games'] = Book.objects.all().order_by('date').reverse()[:10]
    args['cats'] = Category.objects.all()
    args['tags'] = Tag.objects.all()
    args['current_item'] = 'игры'

    # user
    args['username'] = auth.get_user(request).username

    # poll
    args['question_web'] = Question.objects.get(text=u"Как вам наш сайт?")
    args['choices'] = Choice.objects.filter(question_id=args['question_web'].id)

    # books
    all_games = Book.objects.all().order_by('-date')
    current_page = Paginator(all_games, 5)
    args['games'] = current_page.page(page_number)
    args['page_number'] = page_number
    args['count'] = len(Paginator(all_games, 5).page_range)
    return render_to_response('game/games.html', args)
