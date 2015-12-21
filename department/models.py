# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User, UserManager


class Department(models.Model):

    name = models.CharField(verbose_name="Название отдела", max_length=128, blank=True)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = 'Отделы'


class DepartmentJobPosition(models.Model):
    name = models.CharField(verbose_name="Название должности", max_length=128, blank=True)
    department = models.ForeignKey(Department, verbose_name="Отдел")

    def __str__(self):
        return '%s %s' % (self.name, self.department)

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = 'Должности'
