# -*- coding: utf-8 -*-
from django.db import models

try:
    from workers.models import Worker
except ImportError:
    pass


class WorkerSecondaryEducation(models.Model):

    worker = models.ForeignKey(Worker)
    name = models.CharField(max_length=128)
    city = models.CharField(max_length=128, default="Москва")
    from_date = models.DateField(verbose_name="Дата начала обучения")
    to_date = models.DateField(verbose_name="Дата окончания обучения")
    graduation_year = models.PositiveSmallIntegerField(
        verbose_name="Год выпуска", null=True,
        blank=True
    )

    def __str__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = "Среднее общеобразовательное учебное заведение"
        verbose_name_plural = 'Средние общеобразовательные учебные заведения'


class WorkerHighEducation(models.Model):

    worker = models.ForeignKey(Worker)
    name = models.CharField(max_length=128)
    city = models.CharField(max_length=128, default="Москва")
    specialization = models.CharField(max_length=128)
    from_date = models.DateField(verbose_name="Дата начала обучения")
    to_date = models.DateField(verbose_name="Дата окончания обучения")
    graduation_year = models.PositiveSmallIntegerField(
        verbose_name="Год выпуска", null=True,
        blank=True
    )
    education_type = models.CharField(verbose_name="Тип образования", max_length=128)


    def __str__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = "Высшее (среднее специальное) учебное заведение"
        verbose_name_plural = 'Высшие (средние специальные) учебные заведения'
