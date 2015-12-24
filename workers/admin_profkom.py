__author__ = 'tiso'
from django.contrib import admin
from django.contrib.auth.forms import (UserCreationForm, UserChangeForm,
    AdminPasswordChangeForm)
from django.utils.translation import ugettext_lazy as _
# Register your models here.
from .models import WorkerProfkomProxy, WorkerChildProxy, JobPositionReadOnlyProxy, WorkerLocation
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
    template = 'admin/worker/inline_without_add.html'
    model = JobPositionReadOnlyProxy
    verbose_name = "Должность"
    verbose_name_plural = 'Должности'
    extra = 0
    show_change_link = True
    can_delete = False
    readonly_fields = ('worker', 'organization', 'department', 'position', 'current_position',
                       'from_date', 'to_date')


class ChildrenInline(LinkedInline):

    def age(self, child):
        from django.utils import timezone
        if child.birthday is None:
            return None
        return int((timezone.now().date() - child.birthday).total_seconds()/31536000.0)


    model = WorkerChildProxy
    verbose_name = "Ребенок"
    verbose_name_plural = "Список детей"
    extra = 0
    fields = ('age', )
    readonly_fields = ('worker', 'name', 'sex', 'age')
    template = 'admin/worker/inline_without_add.html'
    can_delete = False


class WorkerProfkomProxyAdmin(admin.ModelAdmin):

    change_password_form = AdminPasswordChangeForm
    list_per_page = 10

    list_display = ('last_name', 'first_name', 'patronymic', 'age', 'get_sex', 'get_children_count',
                    'get_current_department',
                    'get_current_job',
                    )
    search_fields = ('last_name', 'first_name', 'patronymic')
    fieldsets = (
        (None, {'fields': ('get_avatar_as_html', )}),
    (_('Personal info'), {'fields': (
        'last_name', 'first_name', 'patronymic', 'sex', 'age', 'marital_status',
    )}),
        (('Новогодние подарки'), {'fields': ('give_gift', 'gifts_in_this_year')}),
    )

    readonly_fields = ('get_avatar_as_html', 'last_name', 'first_name', 'patronymic', 'sex', 'age', 'marital_status',
                       'give_gift', 'gifts_in_this_year')

    inlines = [
        ChildrenInline, JobPositionsInline
    ]
