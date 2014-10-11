#/usr/bin/python
#-*- coding:utf-8 -*-

from django.shortcuts import render, render_to_response
from django.template import loader,Context
from django.http import HttpResponse

import datetime
import collections


# Create your views here.

FIB = [0,1]

def current_datetime(request):
    now = datetime.datetime.now()
    steps = ['手机号码频次统计', '预约地址频次统计', '预约IP地址频次统计']
    t = loader.get_template("index.html")
    c = Context({'ctime':now, 'steps':steps})
    #html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(t.render(c))


def filter_scalper_with_illegalchars(request):
    return HttpResponse('OK!')

def get_fib_sequence():
    global FIB
    FIB.append(FIB[-1] + FIB[-2])
    return FIB

def index(request):
    global FIB
    FIB = [0,1]
    print FIB
    return render_to_response("ref.html", { 'fib_sequence' : [0,1] })

def refresh(request):
    fib_sequence = get_fib_sequence()
    return render_to_response("fib.html", { 'fib_sequence' : fib_sequence })
