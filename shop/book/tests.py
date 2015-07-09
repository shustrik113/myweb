#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import TestCase
from book.models import Book, Publisher, Author, CommentBook
from other.models import Tag, Category, Lang, Unit


class BookTest(TestCase):
    def create_book(self, title="test_book", text="test_text"):
        t = Tag.objects.get(id=1)
        c = Category.objects.get(id=1)
        l = Category.objects.get(id=1)
        u = Unit.objects.get(id=1)
        p = Publisher.objects.get(id=1)
        a = Author.objects.get(id=1)
        pr = 20
        b = Book.objects.create(title=title, text=text, tags=t, cath=c, langs=l,
            unit=u, publisher=p, authors=a, price=pr)
        return b

    def test_book_creation(self):
        b = self.create_book()
        self.assertTrue(isinstance(b, Book))
        self.assertEqual(b.__unicode__(), b.title)

    def test_get_upload_file_name(self):
        filename = "1.jpg"
        path = 'static/images/%s_%s' % (str(time()).replace('.','_')), filename)
        cpath = path + filename
        self.assertEqual(path, cpath)

    def test_books_list_view(self):
        b = self.create_book()
        url = reverse('book.views.books')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b.title, resp.content)

    def test_book_detail_view(self):
        b = self.create_book()
        url = reverse('book.views.book', args=[b.id])
        resp = self.client.get(url)
        self.assertEqual(reverse('book.views.book', args=[b.id]), b.get_absolute_url())
        self.assertEqual(resp.status_code, 200)
        self.assertIn(a.title, resp.content)