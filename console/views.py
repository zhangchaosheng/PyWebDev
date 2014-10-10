#/usr/bin/python
#-*- coding:utf-8 -*-

from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse

import datetime
import collections


# Create your views here.

def current_datetime(request):
    now = datetime.datetime.now()
    steps = ['手机号码频次统计', '预约地址频次统计', '预约IP地址频次统计']
    t = loader.get_template("index.html")
    c = Context({'ctime':now, 'steps':steps})
    #html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(t.render(c))

    
   
