# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views

from .views import ViewWorkers
from security.utils import anonymous_required

urlpatterns = patterns('',
    # url(r'^workers/$', ViewWorkers.as_view())
)
