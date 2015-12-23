from django.contrib import admin
from django.contrib.auth.forms import (UserCreationForm, UserChangeForm,
    AdminPasswordChangeForm)
from django.utils.translation import ugettext_lazy as _
# Register your models here.
from .models import WorkerAdminProxy, WorkerChild, JobPosition, WorkerLocation
from honors.models import SalaryReadOnlyProxy, PrizeReadOnlyProxy, AchievementReadOnlyProxy
from education.models import WorkerHighEducation, WorkerSecondaryEducation

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
    model = SalaryReadOnlyProxy
    readonly_fields = ['salary', 'destination_day']
    verbose_name = "Зарплата"
    verbose_name_plural = "Зарплаты за разные периоды времени"
    extra = 0
    template = 'admin/worker/inline_without_add.html'


class PrizeInline(LinkedInline):
    model = PrizeReadOnlyProxy
    readonly_fields = ['prize', 'destination_day']
    verbose_name = "Премия (последняя указанная премия является текущей)"
    verbose_name_plural = "Премии за разные периоды времени"
    extra = 0
    template = 'admin/worker/inline_without_add.html'


class AchievementInline(LinkedInline):
    model = AchievementReadOnlyProxy
    readonly_fields = ['name', 'achievement_type', 'allowance', 'date']
    verbose_name = "Награждение"
    verbose_name_plural = "Список награжений"
    extra = 0
    template = 'admin/worker/inline_without_add.html'


class ChildrenInline(LinkedInline):
    model = WorkerChild
    verbose_name = "Ребенок"
    verbose_name_plural = "Список детей"
    extra = 0


class LocationInline(TabularInline):
    template = 'admin/worker/location_inline.html'
    model = WorkerLocation
    verbose_name = "Место жительства"
    verbose_name_plural = "Место жительства"
    extra = 0


class SecondaryEducationInline(LinkedInline):
    model = WorkerSecondaryEducation
    verbose_name = "Среднее общеобразовательное учебное заведение"
    verbose_name_plural = "Учебные заведения"
    extra = 0


class HighEducationInline(LinkedInline):
    model = WorkerHighEducation
    verbose_name = "Высшее/средне специальное учебное заведение"
    verbose_name_plural = "Высшие/среднеспециальные учебные заведения"
    extra = 0


class WorkerAdminProxyAdmin(admin.ModelAdmin):

    change_password_form = AdminPasswordChangeForm
    list_per_page = 10

    list_display = ('last_name', 'first_name', 'patronymic', 'age', 'get_sex', 'get_children_count',
                    'get_current_department',
                    'get_current_job', 'get_current_white_salary', 'get_current_tax', 'salary_by_current_year'
                    )
    search_fields = ('last_name', 'first_name', 'patronymic')
    fieldsets = (
        (None, {'fields': ('get_avatar_as_html', 'avatar', 'username', 'password')}),
    (_('Personal info'), {'fields': (
        'last_name', 'first_name', 'patronymic', 'sex', 'birthday', 'birth_place', 'email', 'marital_status',
    )}),
    )

    readonly_fields = ('get_avatar_as_html', )

    inlines = [
        ChildrenInline, JobPositionsInline, LocationInline,
        SecondaryEducationInline, HighEducationInline, SalaryInline, PrizeInline, AchievementInline,
    ]
