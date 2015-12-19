# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User, UserManager


class Department(models.Model):

    name = models.CharField(verbose_name="Название отдела", max_length=128, blank=True)

    def __unicode__(self):
        return u'%s' % self.name