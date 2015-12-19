from django.contrib import admin
from django import forms
from .models import Salary, Prize, Achievement, SalaryReadOnlyProxy, \
    AchievementReadOnlyProxy, PrizeReadOnlyProxy
# Register your models here.

admin.site.register(Salary, admin.ModelAdmin)
admin.site.register(Prize, admin.ModelAdmin)
admin.site.register(Achievement, admin.ModelAdmin)


class SalaryReadonlyProxyAdmin(admin.ModelAdmin):
    list_display = ['worker', 'salary', 'destination_day']
    readonly_fields = ['worker', 'salary', 'destination_day']

admin.site.register(SalaryReadOnlyProxy, SalaryReadonlyProxyAdmin)


class AchievementReadOnlyProxyAdmin(admin.ModelAdmin):
    list_display = ['worker', 'name', 'achievement_type', "allowance", "date"]
    readonly_fields = ['worker', 'name', 'achievement_type', "allowance", "date"]

admin.site.register(AchievementReadOnlyProxy, AchievementReadOnlyProxyAdmin)


class PrizeReadOnlyProxyAdmin(admin.ModelAdmin):
    list_display = ['worker', 'prize']
    readonly_fields = ['worker', 'prize']

admin.site.register(PrizeReadOnlyProxy, PrizeReadOnlyProxyAdmin)


