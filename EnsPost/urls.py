from django.conf.urls import url
from django.urls import path
from .views import *

app_name = 'post'

urlpatterns = [

    url('index/$', post_index, name= 'index'),
    url('(?P<id>\d+)/$', post_detail, name= 'detail'),
    url('create/$', post_create, name= 'create'),
    url('(?P<id>\d+)/update/$', post_update, name= 'update'),
    url('(?P<id>\d+)/delete/$', post_delete, name= 'delete'),
]