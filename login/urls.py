# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views

from .views import LoginView, view_logout
from security.utils import anonymous_required

urlpatterns = patterns('',
    url(r'^accounts/login/$', anonymous_required(LoginView.as_view()), name="login"),
    url(r'^accounts/logout/$', view_logout, name="logout"),
)
