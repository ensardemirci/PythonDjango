from django.conf.urls import url
from django.urls import path
from .views import *

app_name = 'post'

urlpatterns = [

    url('create/$', post_create, name='create'),
    url('index/$', post_index, name= 'index'),


    url('(?P<slug>[\w-]+)/update/$', post_update, name='update'),
    url('(?P<slug>[\w-]+)/delete/$', post_delete, name= 'delete'),
    url('(?P<slug>[\w-]+)/$', post_detail, name='detail'),
]