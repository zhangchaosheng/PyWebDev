from django.conf.urls import *
from console.views import *

 
urlpatterns = patterns('',
    url(r'refresh', refresh),
    url(r'step1/$', filter_scalper_with_illegalchars),
    #url(r'$', current_datetime),
    url(r'$', index),
)
