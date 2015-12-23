from django.contrib import admin
from django.contrib.auth.forms import (UserCreationForm, UserChangeForm,
    AdminPasswordChangeForm)
from django.utils.translation import ugettext_lazy as _
# Register your models here.
from .models import Worker, WorkerChild, JobPosition, WorkerLocation
from honors.models import Salary, Prize, Achievement
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


class WorkerAdmin(admin.ModelAdmin):

    change_password_form = AdminPasswordChangeForm

    list_display = ('last_name', 'first_name', 'patronymic', 'age', 'get_sex', 'get_children_count',
                    'get_current_department',
                    'get_current_job', 'get_current_white_salary', 'get_current_tax', 'salary_by_current_year'
                    )
    fieldsets = (
        (None, {'fields': ('get_avatar_as_html', 'avatar', 'username', 'password')}),
    (_('Personal info'), {'fields': (
        'last_name', 'first_name', 'patronymic', 'sex', 'birthday', 'birth_place', 'email', 'marital_status',
    )}),
    (_('Permissions'), {'fields': ('is_active', 'is_staff', 'user_type')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Groups'), {'fields': ('groups',)}),
    )

    readonly_fields = ('get_avatar_as_html', )

    inlines = [
        JobPositionsInline, SalaryInline, PrizeInline, AchievementInline, ChildrenInline, LocationInline,
        SecondaryEducationInline, HighEducationInline
    ]

admin.site.register(Worker, WorkerAdmin)
admin.site.register(WorkerChild, admin.ModelAdmin)
admin.site.register(JobPosition, admin.ModelAdmin)