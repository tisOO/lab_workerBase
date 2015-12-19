# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractUser

from department.models import Department


MARITAL_STATUS = (
    ("Single", "Не женат"),
    ("In relation ship", "Встречаюсь"),
    ("Engaged", "Помолвлен(а)"),
    ("Married", "Женат/замужем"),
    ("In love", "Влюбен(а)"),
    ("It's complicated", "Все сложно"),
    ("Actively searching", "В активном поиске"),
    ("I'm programmer", "Я - программист")

)

USER_TYPES = (
    ("Admin", "Администратор"),
    ("Human resources Department", "Отдел кадров"),
    ("Accounting", "Бухгалтерия"),
    ("Chief", "Начальник"),
    ("Trade union", "Профком")
)


class Worker(AbstractUser):

    user_type = models.CharField(verbose_name="Тип пользователя", choices=USER_TYPES, max_length=64, null=True)
    patronymic = models.CharField(verbose_name="Отчество", max_length=255, null=True)
    sex = models.BooleanField(verbose_name="Пол", default=False)
    birth_place = models.CharField(verbose_name="Место рождения", max_length=255, null=True)
    birthday = models.DateField(verbose_name="Дата рождения", null=True)
    marital_status = models.CharField(verbose_name="Семейное положение", choices=MARITAL_STATUS,
                                      max_length=50, null=True)
    avatar = models.ImageField(upload_to='images/web_users/', blank=True, null=True, help_text='User\'s avatar')

    objects = UserManager()

    class Meta:
        ordering = ['id']

    def __unicode__(self):
        return u'%s %s %s' % (self.last_name, self.first_name, self.patronymic)


class WorkerChild(models.Model):

    worker = models.ForeignKey(Worker)
    name = models.CharField(verbose_name="Имя ребенка", max_length=255)
    last_name = models.CharField(verbose_name="Фамилия ребенка", max_length=255)
    patronymic = models.CharField(verbose_name="Отчество ребенка", max_length=255)
    birthday = models.DateField(verbose_name="Дата рождения ребенка")

    def __unicode__(self):
        return u'%s %s %s' % (self.last_name, self.name, self.patronymic)


class JobPosition(models.Model):

    worker = models.ForeignKey(Worker)
    organization = models.CharField(verbose_name="Название организации", max_length=128, blank=True)
    department = models.ForeignKey(Department, null=True)
    position = models.CharField(verbose_name="Должность", max_length=128)
    from_date = models.DateField(verbose_name="Дата начала работы на данной позиции")
    to_date = models.DateField(verbose_name="Дата окончания работы на данной позиции")