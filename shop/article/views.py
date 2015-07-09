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

from models import Article, Comment
from other.models import Category, Tag, Question, Choice, Menu
from book.models import Book
from forms import CommentForm


def auth_required(function):
    def check_auth(request):
        if not request.user.is_authenticated():
            return HttpResponseRedirect("/other/loginpage/")
        return function(request)
    return check_auth


# ALL ARTICLES
def articles(request, page_number=1):
    args = {}
    args.update(csrf(request))
    args['menu'] = Menu.objects.all()
    args['this_page'] = '/articles/'

    # right box
    args['pop_articles'] = Article.objects.all().order_by('-likes')[:10]
    args['new_articles'] = Article.objects.all().order_by('-date')[:10]
    args['cats'] = Category.objects.all()
    args['tags'] = Tag.objects.all()
    args['current_item'] = 'статьи'

    # user
    args['username'] = auth.get_user(request).username

    # poll
    args['question_web'] = Question.objects.get(text=u"Как вам наш сайт?")
    args['choices'] = Choice.objects.filter(question_id=args['question_web'].id)

    # articles
    all_articles = Article.objects.all().order_by('-date')
    for article in all_articles:
        t = article.text
        t_num = len(t.split(' '))
        if t_num > 40:
            t_pre = t[:410]
            t_res = t_pre + '...'
            article.text = t_res

    current_page = Paginator(all_articles, 5)
    args['articles'] = current_page.page(page_number)
    args['page_number'] = page_number
    args['count'] = len(Paginator(all_articles, 5).page_range)
    return render_to_response('article/articles.html', args)


# Articles by category
def articles_cat(request, cat_slug, page_number=1):
    args = {}
    args.update(csrf(request))
    args['menu'] = Menu.objects.all()
    args['this_page'] = '/articles_cat/'
    args['cat_slug'] = cat_slug

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

    try:
        cat = Category.objects.get(slug=cat_slug)
        all_articles = Article.objects.filter(cath=cat).order_by('-date')

        for article in all_articles:
            article_id = article.id
            comments = Comment.objects.filter(article_id=article_id)
            article.num_comments = len(comments)

            t = article.text
            t_num = len(t.split(' '))
            if t_num > 40:
                t_pre = t[:400]
                t_res = t_pre + '...'
                article.text = t_res

        current_page = Paginator(all_articles, 5)
        args['articles'] = current_page.page(page_number)
        args['page_number'] = page_number
        args['count'] = len(Paginator(all_articles, 5).page_range)
        return render_to_response('article/articles_cat.html', args)
    except Category.DoesNotExist:
        raise Http404('Category does not exist')


# Articles by tag
def tag(request, tag_slug, page_number=1):
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

    try:
        tag = Tag.objects.filter(slug=tag_slug)
        all_articles = Article.objects.filter(tags=tag).order_by('date')
        current_page = Paginator(all_articles, 5)
        args['articles'] = current_page.page(page_number)
        args['page_number'] = page_number
        args['count'] = len(Paginator(all_articles, 5).page_range)
        return render_to_response('article/articles.html', args)
    except Category.DoesNotExist:
        raise Http404()


# Only one article
def article(request, article_id=1, page_number=1):
    # right box
    comment_form = CommentForm
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

    args['article'] = Article.objects.get(id=article_id)
    args['article_tags'] = args['article'].tags.all()
    args['form'] = comment_form
    all_comments = Comment.objects.filter(article_id=article_id)

    current_page = Paginator(all_comments, 5)
    args['comments'] = current_page.page(page_number)
    args['page_number'] = page_number
    args['count'] = len(Paginator(all_comments, 5).page_range)
    return render_to_response('article/article.html', args)


# Add like
def addlike(request):
    if request.POST:
        article_id = request.POST['article_id']
        article_id = int(article_id)
        try:
            if article_id in request.COOKIES:
                pass
            else:
                article = Article.objects.get(id=article_id)
                article.likes += 1
                article.save()
                # response = redirect('/articles/')
                # response.set_cookie(article_id, "test")
        except ObjectDoesNotExist:
            raise Http404

        args = {}
        args.update(csrf(request))
        args['likes'] = article.likes
    return render_to_response('likes.html', args)


# Add comment
def addcomment(request, article_id):
    if request.POST and ("pause" not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = Article.objects.get(id=article_id)
            comment.date = datetime.datetime.now()
            comment.user = auth.get_user(request)
            form.save()

            request.session.set_expiry(60)
            request.session["pause"] = True
            article = Article.objects.get(id=article_id)
            article.num_comments += 1
            article.save()
    return redirect('/articles/article/%s' % article_id + '/#comment')


# Add like
def addlike_Comment(request, comment_id):
    try:
        if comment_id in request.COOKIES:
            redirect('/articles/')
        else:
            comment = Comment.objects.get(id=comment_id)
            comment.likes += 1
            comment.save()
            response = redirect('/articles/')
            response.set_cookie(comment_id, "test")
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/articles/')


# Add article
def newArticle(request):
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
    args.update(csrf(request))
    return render_to_response('article/new_article.html', args)


# for saving article:
TagDelim = re.compile(ur'\s*,\s*')


# save article
def saveArticle(request):
    # right box
    menu = Menu.objects.all()
    pop_articles = Article.objects.all().order_by('likes').reverse()[:10]
    new_articles = Article.objects.all().order_by('date').reverse()[:10]
    cats = Category.objects.all()
    tags = Tag.objects.all()
    current_item = 'статьи'

    # user
    username = auth.get_user(request).username

    # poll
    question_web = Question.objects.get(text=u"Как вам наш сайт?")
    choices = Choice.objects.filter(question_id=question_web.id)

    if request.POST:
        # test = request.FILES
        # return render_to_response('test.html', locals())

        user_agent = request.META['HTTP_USER_AGENT']
        title = request.POST['article_title']
        text = request.POST['article_text']
        cath = Category.objects.get(slug=request.POST['article_cath'])
        a_tags = request.POST['article_tags'].strip()
        date = datetime.datetime.now()
        user = request.user
        # ispriv = request.GET['article_is_private']

        if request.FILES['article_image']:
            img = request.FILES['article_image']
            img_path = 'static/images/articles/'
            image = img_path + str(img)
            content = ContentFile(request.FILES['article_image'].read())
            article = Article(title=title, text=text, cath=cath, image=image, date=date, user=user)
            article.image.save(str(img), content, save=True)
        else:
            article = Article(title=title, text=text, cath=cath, date=date, user=user)
            article.save()

        for tag in TagDelim.split(a_tags):
            if tag == '':
                tag = 'тест'
            tag = tag.lower()
            try:
                T = Tag.objects.get(name=tag)
            except Tag.DoesNotExist:
                T = Tag(name = tag)
                T.save()
            article.tags.add(T)

        article_tags = article.tags.all()

        for cat in cats:
            myCat = Category.objects.get(slug=cat.slug)
            a = len(Article.objects.filter(cath=myCat))
            b = len(Book.objects.filter(cath=myCat))
            cat.items = a + b
            cat.save()

    return render_to_response('article/article_saved.html', locals())
