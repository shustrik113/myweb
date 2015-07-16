#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from django.core.context_processors import csrf

# from django.contrib.auth.forms import UserCreationForm
# from django.core.paginator import Paginator
# from django.contrib import auth

from article.models import Article, Comment, Game, GameComment
from forms import CommentForm


# starting website
def index(reques):
    args = {}

    all_articles = Article.objects.all().order_by('-date')
    for article in all_articles:
        t = article.text
        t_num = len(t.split(' '))
        if t_num > 40:
            t_pre = t[:800]
            t_res = t_pre + '...'
            article.text = t_res

    args['articles'] = all_articles
    args['ten_comments'] = Comment.objects.all().order_by('-date')[:10]
    args['ten_articles'] = Article.objects.all().order_by('-date')[:10]
    args['this_page'] = 'index'
    return render_to_response('index.html', args)


# one article
def article(request, article_id=1):
    args = {}
    args.update(csrf(request))
    args['form'] = CommentForm
    args['articles'] = Article.objects.all()
    args['article'] = Article.objects.get(id=article_id)
    args['ten_articles'] = Article.objects.all().order_by('-date')[:10]
    args['ten_comments'] = Comment.objects.all().order_by('-date')[:10]
    args['comments'] = Comment.objects.filter(article_id=article_id)
    return render_to_response('article.html', args)


# Add like
def addlike(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        article.likes += 1
        article.save()
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')


# Add comment
def addcomment(request, article_id):
    if request.POST and ['pause' not in request.session]:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = Article.objects.get(id=article_id)
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/article/%s/' % article_id)


# Literature games
def games(request):
    args = {}
    args['articles'] = Article.objects.all()
    args['ten_comments'] = Comment.objects.all()[:10]
    args['games'] = Game.objects.all()
    return render_to_response('games.html', args)


# one game with comments
def game(request, game_id=1):
    args = {}
    args.update(csrf(request))
    args['form'] = CommentForm
    args['game'] = Game.objects.get(id=game_id)
    args['ten_comments'] = Comment.objects.all()[:10]
    args['game_comments'] = GameComment.objects.filter(comment_game_id=game_id)
    return render_to_response('game.html', args)
