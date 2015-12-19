# -*- coding: utf-8 -*-

from django import forms

'''

В этом файле описываются формы,
необходимые для осуществления
логина в систему

'''


class LoginForm(forms.Form):

    username = forms.CharField(max_length=30, label="")
    password = forms.CharField(max_length=50, widget=forms.PasswordInput, label="")

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = u'Логин'
        self.fields['username'].widget.attrs['id'] = u'inputEmail'
        self.fields['password'].widget.attrs['placeholder'] = u'Пароль'
        self.fields['password'].widget.attrs['type'] = u'password'

# class LoginForm(forms.Form):
#     class Meta:
#         fields = ['username', 'password']
#         widgets = {
#             'username': forms.TextInput(attrs = {'placeholder': 'Логин', 'max_length': 30}),
#             'password': forms.PasswordInput(attrs = {'placeholder': 'Пароль', 'max_length': 50})
#         }