#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, redirect
from django.http.response import HttpResponse, Http404
from django.contrib import auth
from django.core.context_processors import csrf
from django.core import serializers
import json

from models import Gamer


# Main page
def start(request):
    args = {}
    gamers = Gamer.objects.all()[:10]
    args["gamers"] = gamers
    return render_to_response('index.html', args)


# Starting game
def game(request):
    args = {}
    args.update(csrf(request))
    gamer = Gamer.objects.get(gamer_name="Sergey")
    gamers = Gamer.objects.all().order_by('gamer_best_result').reverse()[:10]
    args["gamers"] = gamers
    args["gamer"] = gamer
    return render_to_response('game.html', args)


# Snakes search
def snakes(request):
    return render_to_response('snakes.html', {})


# Saving records
def saveRes(request):
    if request.POST:
        args = {}
        args.update(csrf(request))
        gamer = Gamer.objects.get(gamer_name="Sergey")
        new = int(request.POST.get('last_result', ''))
        gamer.gamer_last_result = new

        if (gamer.gamer_last_result > gamer.gamer_best_result):
            gamer.gamer_best_result = gamer.gamer_last_result

        gamer.save()
        args["gamer"] = gamer
    return redirect('/game/')


# Show records
def showRecords(request):
    if request.GET:
        gamers = Gamer.objects.all().order_by('gamer_best_result').reverse()[:10]
        gamers_json_str = serializers.serialize("json", gamers)
    return HttpResponse(gamers_json_str)


# This code ignore please (it's very WIP yet):
def login(request):
    args = {}
    args.update(csrf(request))
    args.update(request)
    if request.POST:
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Not correct data"
            return redirect('/')
    else:
        return redirect('/')
        # render_to_response('index.html', args)

def logout(request):
    auth.logout(request)
    return redirect('/')

