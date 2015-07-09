#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.files.base import ContentFile

from django.shortcuts import render_to_response, redirect
from django.http import Http404, HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth

from models import UserProfile
from forms import UserProfileForm

from article.models import Article, Comment
from other.models import Category, Tag, Question, Choice, Menu


# current user profile
@login_required
def user_profile(request):
    if request.POST:
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            user = request.user
            profile = user.profile
            user.first_name = profile.first_name
            user.last_name = profile.last_name
            user.save()
            profile.save()
            return HttpResponseRedirect('/users/profile_current_user/')
    else:
        user = request.user
        profile = user.profile
        form = UserProfileForm(instance=profile)

    args = {}
    args.update(csrf(request))
    args['menu'] = Menu.objects.all()
    args['this_page'] = '/profile/'

    # right box
    args['pop_articles'] = Article.objects.all().order_by('-likes')[:10]
    args['new_articles'] = Article.objects.all().order_by('-date')[:10]
    args['cats'] = Category.objects.all()
    args['tags'] = Tag.objects.all()
    args['current_item'] = 'статьи'

    # user
    args['username'] = request.user

    # poll
    args['question_web'] = Question.objects.get(text=u"Как вам наш сайт?")
    args['choices'] = Choice.objects.filter(question_id=args['question_web'].id)

    args['form'] = form
    return render_to_response('users/profile_current_user.html', args)


# Profile of some other user
def some_user_profile(request, user):
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
    args['username'] = auth.get_user(request).username

    # poll
    args['question_web'] = Question.objects.get(text=u"Как вам наш сайт?")
    args['choices'] = Choice.objects.filter(question_id=args['question_web'].id)

    # profile
    args['empty'] = 'не указано'
    user = User.objects.get(username=user)
    args['name'] = user
    args['email'] = user.email
    args['first_name'] = user.first_name
    args['last_name'] = user.last_name
    args['date_joined'] = user.date_joined
    args['last_login'] = user.last_login
    return render_to_response('users/profile_some_user.html', args)


# AUTHENTICATION
# Login page
def loginPage(request):
    args = {}
    args.update(csrf(request))
    args['menu'] = Menu.objects.all()
    args['this_page'] = 'enter'

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
    return render_to_response('users/login.html', args)


# Forgot password page
def forgotPass(request):
    # right box
    args = {}
    args.update(csrf(request))
    args['menu'] = Menu.objects.all()
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
    return render_to_response('users/forgot_pass.html', args)


# Login user
def login(request):
    args = {}
    args.update(csrf(request))
    args['menu'] = Menu.objects.all()
    if request.POST:
        u = request.POST.get('username', '')
        p = request.POST.get('password', '')
        user = auth.authenticate(username=u, password=p)
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('/')
        else:
            args['pop_articles'] = Article.objects.all().order_by('likes').reverse()[:10]
            args['new_articles'] = Article.objects.all().order_by('date').reverse()[:10]
            args['cats'] = Category.objects.all()
            args['tags'] = Tag.objects.all()
            args['current_item'] = 'статьи'

            # poll
            args['question_web'] = Question.objects.get(text=u"Как вам наш сайт?")
            args['choices'] = Choice.objects.filter(question_id=args['question_web'].id)
            args['login_error'] = "Логин или пароль не корректен"
            return render_to_response('login.html', args)
    else:
        return render_to_response('users/login.html', locals())


# Log out user
def logout(request):
    auth.logout(request)
    return redirect('/')


# Register user
def register(request):
    if request.POST:
        u = request.POST.get('username', '')
        p = request.POST.get('password', '')
        e = request.POST.get('email', '')
        user = User.objects.create_user(username=u, password=p, email=e)
        user.save()

        user = auth.authenticate(username=u, password=p)
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('/')
    return redirect('/')









