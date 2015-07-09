#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    M = u'Мужской'
    F = u'Женский'
    N = u'Неизвестно'
    SEX = (
        (M, u'Мужской'),
        (F, u'Женский'),
        (N, u'Неизвестно'),
    )

    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=50, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=50, blank=True, verbose_name='Фамилия')
    city = models.CharField(max_length=50, blank=True, verbose_name='Город')
    sex = models.CharField(max_length=10, choices=SEX, default=N, verbose_name='Пол')
    birthday = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    ava = models.ImageField(upload_to="static/images/avatars/", blank=True, null=True, verbose_name='Аватар')
    skype = models.CharField(blank=True, max_length=30, verbose_name='Skype')
    likes_got = models.IntegerField(default=0)
    num_pub = models.IntegerField(default=0)
    is_priv_email = models.BooleanField(default=False)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])