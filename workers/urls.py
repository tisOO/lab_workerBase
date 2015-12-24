# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views

from .views import ViewWorkers, give_gift
from security.utils import anonymous_required

urlpatterns = patterns('',
    # url(r'^workers/$', ViewWorkers.as_view())
    url(r'^gift/(?P<worker>\d+)/$', give_gift)
)
