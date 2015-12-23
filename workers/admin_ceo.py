from django.contrib import admin
from django.contrib.auth.forms import (UserCreationForm, UserChangeForm,
    AdminPasswordChangeForm)
from django.utils.translation import ugettext_lazy as _
# Register your models here.
from .models import WorkerCEOProxy, WorkerChildProxy, JobPosition, WorkerLocationProxy
from honors.models import Salary, Prize, Achievement
from education.models import WorkerHighEducationProxy, WorkerSecondaryEducationProxy

from django.contrib.admin.options import InlineModelAdmin, TabularInline


class LinkedInline(InlineModelAdmin):
    template = 'admin/worker/job_inline.html'
    admin_model_path = None

    def __init__(self, *args):
        super(LinkedInline, self).__init__(*args)
        if self.admin_model_path is None:
            self.admin_model_path = self.model.__name__.lower()


class JobPositionsInline(LinkedInline):
    model = JobPosition
    verbose_name = "Должность"
    verbose_name_plural = 'Должности'
    extra = 0
    show_change_link = True


class SalaryInline(LinkedInline):
    model = Salary
    verbose_name = "Зарплата"
    verbose_name_plural = "Зарплаты за разные периоды времени"
    extra = 0


class PrizeInline(LinkedInline):
    model = Prize
    verbose_name = "Премия (последняя указанная премия является текущей)"
    verbose_name_plural = "Премии за разные периоды времени"
    extra = 0


class AchievementInline(LinkedInline):
    model = Achievement
    verbose_name = "Награждение"
    verbose_name_plural = "Список награжений"
    extra = 0


class ChildrenInline(LinkedInline):
    model = WorkerChildProxy
    verbose_name = "Ребенок"
    verbose_name_plural = "Список детей"
    extra = 0
    readonly_fields = ('worker', 'name', 'sex', 'birthday')
    template = 'admin/worker/inline_without_add.html'


class LocationInline(TabularInline):
    template = 'admin/worker/inline_without_add.html'
    model = WorkerLocationProxy
    verbose_name = "Место жительства"
    verbose_name_plural = "Место жительства"
    extra = 0
    readonly_fields = ('worker', 'city', 'street', 'house', 'flat')
    can_delete = False


class SecondaryEducationInline(LinkedInline):
    model = WorkerSecondaryEducationProxy
    verbose_name = "Среднее общеобразовательное учебное заведение"
    verbose_name_plural = "Учебные заведения"
    extra = 0
    readonly_fields = ('worker', 'name', 'city', 'from_date', 'to_date', 'graduation_year')
    can_delete = False
    template = 'admin/worker/inline_without_add.html'


class HighEducationInline(LinkedInline):
    model = WorkerHighEducationProxy
    verbose_name = "Высшее/средне специальное учебное заведение"
    verbose_name_plural = "Высшие/среднеспециальные учебные заведения"
    extra = 0
    readonly_fields = ('worker', 'name', 'city', 'specialization', 'from_date', 'to_date', 'graduation_year', 'education_type')
    can_delete = False
    template = 'admin/worker/inline_without_add.html'


class WorkerCEOProxyAdmin(admin.ModelAdmin):

    change_password_form = AdminPasswordChangeForm
    list_per_page = 10

    list_display = ('last_name', 'first_name', 'patronymic', 'age', 'get_sex', 'get_children_count',
                    'get_current_department',
                    'get_current_job', 'get_current_white_salary', 'get_current_tax', 'salary_by_current_year'
                    )
    fieldsets = (
        (None, {'fields': ('get_avatar_as_html', )}),
    (_('Personal info'), {'fields': (
        'last_name', 'first_name', 'patronymic', 'sex', 'birthday', 'birth_place', 'email', 'marital_status',
    )}),
    )

    search_fields = ('last_name', 'first_name', 'patronymic')

    readonly_fields = (
        'get_avatar_as_html', 'last_name', 'first_name', 'patronymic', 'sex', 'birthday',
        'birth_place', 'email', 'marital_status',
        'is_active', 'is_staff', 'user_type'

    )

    inlines = [
        ChildrenInline, JobPositionsInline, LocationInline,
        SecondaryEducationInline, HighEducationInline, SalaryInline, PrizeInline, AchievementInline,
    ]
