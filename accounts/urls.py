from django.conf.urls import url
from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [

    url('login/$', login_view, name='login'),
    url('register/$', register_view, name='register'),
    url('logout/$', logout_view, name='logout'),
    ]
