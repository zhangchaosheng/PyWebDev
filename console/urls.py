from django.conf.urls import *
from console.views import current_datetime

 
urlpatterns = patterns('',
    url(r'time/$', current_datetime),
)
