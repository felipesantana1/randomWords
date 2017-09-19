# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def randomWord(request):
    request.session['randomWord'] = get_random_string(length=14)
    request.session['attempts'] = 0
    return render(request, 'random_words/index.html')

def newRandom(request):
    if request.method == 'POST':
        request.session['randomWord'] = get_random_string(length=14)
        request.session['attempts'] += 1
    return render(request, 'random_words/index.html')

def attemptReset(request):
    if request.method == 'POST':
        return redirect('/random_word')
    return redirect('/')