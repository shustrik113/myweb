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

from models import Book, Publisher, Author, CommentBook
from other.models import Category, Tag, Unit, Question, Choice, Menu
from forms import BookForm, CommentForm


# ALL BOOKS
def books(request, page_number=1):
    # right box
    args = {}
    args.update(csrf(request))
    args['this_page'] = '/books/'
    args['menu'] = Menu.objects.all()
    args['pop_books'] = Book.objects.all().order_by('-likes')[:10]
    args['new_books'] = Book.objects.all().order_by('-date')[:10]
    args['cats'] = Category.objects.all()
    args['tags'] = Tag.objects.all()
    args['current_item'] = 'книги'

    # user
    args['username'] = auth.get_user(request).username

    # poll
    args['question_web'] = Question.objects.get(text=u"Как вам наш сайт?")
    args['choices'] = Choice.objects.filter(question_id=args['question_web'].id)

    # books
    all_books = Book.objects.all().order_by('-date')
    current_page = Paginator(all_books, 5)
    args['books'] = current_page.page(page_number)
    args['page_number'] = page_number
    args['count'] = len(Paginator(all_books, 5).page_range)
    return render_to_response('book/books.html', args)


# adding new book
def create_book(request):
    if request.POST:
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/books/')
    else:
        form = BookForm()

    args = {}
    args.update(csrf(request))
    args['form'] = form

    # right box
    args['menu'] = Menu.objects.all()
    args['pop_books'] = Book.objects.all().order_by('likes').reverse()[:10]
    args['new_books'] = Book.objects.all().order_by('date').reverse()[:10]
    args['cats'] = Category.objects.all()
    args['tags'] = Tag.objects.all()
    args['current_item'] = 'книги'

    # user
    args['username'] = auth.get_user(request).username

    # poll
    args['question_web'] = Question.objects.get(text=u"Как вам наш сайт?")
    args['choices'] = Choice.objects.filter(question_id=args['question_web'].id)
    return render_to_response('book/create_book.html', args)


# adding comment to book
def add_comment(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.POST:
        f = CommentForm(request.POST)
        if f.is_valid():
            c = f.save(commit=False)
            c.book = book
            c.save()
            return HttpResponseRedirect('/books/book/%s' % books_id)
    else:
        f = CommentForm()

    args = {}
    args.update(csrf(request))
    args['book'] = book
    args['form'] = f

    # right box
    args['menu'] = Menu.objects.all()
    args['pop_books'] = Book.objects.all().order_by('likes').reverse()[:10]
    args['new_books'] = Book.objects.all().order_by('date').reverse()[:10]
    args['cats'] = Category.objects.all()
    args['tags'] = Tag.objects.all()
    args['current_item'] = 'книги'

    # user
    args['username'] = auth.get_user(request).username

    # poll
    args['question_web'] = Question.objects.get(text=u"Как вам наш сайт?")
    args['choices'] = Choice.objects.filter(question_id=args['question_web'].id)
    return render_to_response('book/book.html', args)


# Books by category
def books_cat(request, cat_slug, page_number=1):
    args = {}
    args.update(csrf(request))
    args['menu'] = Menu.objects.all()
    args['this_page'] = '/books_cat/'
    args['cat_slug'] = cat_slug

    # right box
    args['pop_books'] = Book.objects.all().order_by('-likes')[:10]
    args['new_books'] = Book.objects.all().order_by('-date')[:10]
    args['cats'] = Category.objects.all()
    args['tags'] = Tag.objects.all()
    args['current_item'] = 'книги'

    # user
    args['username'] = request.user

    # poll
    args['question_web'] = Question.objects.get(text=u"Как вам наш сайт?")
    args['choices'] = Choice.objects.filter(question_id=args['question_web'].id)

    try:
        cat = Category.objects.get(slug=cat_slug)
        all_books = Book.objects.filter(cath=cat).order_by('-date')

        for book in all_books:
            book_id = book.id
            comments = CommentBook.objects.filter(book_id=book_id)
            book.num_comments = len(comments)

        current_page = Paginator(all_books, 5)
        args['books'] = current_page.page(page_number)
        args['page_number'] = page_number
        args['count'] = len(Paginator(all_books, 5).page_range)
        return render_to_response('book/books_cat.html', args)
    except Category.DoesNotExist:
        raise Http404('Category does not exist')


# One book
def book(request, book_slug='s20150706134315377', page_number=1):
    args = {}
    comment_form = CommentForm
    args.update(csrf(request))
    args['menu'] = Menu.objects.all()

    # right box
    args['pop_books'] = Book.objects.all().order_by('-likes')[:10]
    args['new_books'] = Book.objects.all().order_by('-date')[:10]
    args['cats'] = Category.objects.all()
    args['tags'] = Tag.objects.all()
    args['current_item'] = 'книги'
    args['this_page'] = '/books_cat/'

    # user
    args['username'] = request.user

    # poll
    args['question_web'] = Question.objects.get(text=u"Как вам наш сайт?")
    args['choices'] = Choice.objects.filter(question_id=args['question_web'].id)

    args['book'] = Book.objects.get(slug=book_slug)
    args['book_tags'] = args['book'].tags.all()
    args['form'] = comment_form
    book_id = args['book'].id
    all_comments = CommentBook.objects.filter(book_id=book_id)

    current_page = Paginator(all_comments, 5)
    args['comments'] = current_page.page(page_number)
    args['page_number'] = page_number
    args['count'] = len(Paginator(all_comments, 5).page_range)
    return render_to_response('book/book.html', args)