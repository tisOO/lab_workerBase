# -*- coding: utf-8 -*-

from django.db import models

try:
    from workers.models import Worker
except ImportError:
    pass


class Salary(models.Model):
    worker = models.ForeignKey(Worker)
    salary = models.PositiveSmallIntegerField(verbose_name="Зарплата")
    destination_day = models.DateField(verbose_name="День с которого действует зарплата")

    def __str__(self):
        return "Зарплата: %s рублей, начиная с %s" % (self.salary, self.destination_day)

    class Meta:
        verbose_name = "Зарплата"
        verbose_name_plural = 'Зарплаты'


class SalaryReadOnlyProxy(Salary):
    class Meta:
        proxy = True
        verbose_name = "Зарплата"
        verbose_name_plural = 'Зарплаты'


class Prize(models.Model):
    worker = models.ForeignKey(Worker)
    prize = models.PositiveSmallIntegerField(verbose_name="Процент премии")
    destination_day = models.DateField(verbose_name="Дата назначения премии")

    class Meta:
        verbose_name = "Премия"
        verbose_name_plural = 'Премии'
        ordering = ['-id']

    def __str__(self):
        return "Премия: %s рублей" % self.prize


class PrizeReadOnlyProxy(Prize):
    class Meta:
        proxy = True
        verbose_name = "Премия"
        verbose_name_plural = 'Премии'


ACHIEVEMENT_TYPE = (
    ("promo", "Поощрение"),
    ("recovery", "Взыскание")
)


class Achievement(models.Model):
    worker = models.ForeignKey(Worker)
    name = models.CharField(verbose_name="Название события", max_length=128)
    achievement_type = models.CharField(verbose_name="Тип события", choices=ACHIEVEMENT_TYPE, max_length=32)
    allowance = models.IntegerField(verbose_name="Надбавка (может быть отрицательной)")
    date = models.DateField(verbose_name="Дата награждения/взыскания")

    class Meta:
        verbose_name = "Награждение/взыскание"
        verbose_name_plural = 'Награждения/взыскания'


class AchievementReadOnlyProxy(Achievement):
    class Meta:
        proxy = True
        verbose_name = "Награждение/взыскание"
        verbose_name_plural = 'Награждения/взыскания'
