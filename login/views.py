# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.views.generic.base import View

from .forms import LoginForm


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        return render(request, 'login/login.html', {'login_form': login_form})

    def post(self, request):

        login_form = LoginForm(request.POST)
        error = ''

        if login_form.is_valid():
            cd = login_form.cleaned_data

            user = auth.authenticate(username=cd['username'], password=cd['password'])

            if user is not None and user.is_active:
                auth.login(request, user)
                if 'next' in request.GET:
                    return HttpResponseRedirect(request.GET['next'])
                return HttpResponseRedirect('/')
            else:
                error = 'Войти в систему не удалось. Проверьте введенные данные'


        return render(request, 'login/login.html', {'login_form': login_form,
                                              'error': error})


def view_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')