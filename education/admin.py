from django.contrib import admin
from .models import WorkerSecondaryEducation, WorkerHighEducation
# Register your models here.


class SecEduAdmin(admin.ModelAdmin):

    list_display = ('worker', 'name', 'city', 'from_date', 'to_date', 'graduation_year')
    search_fields = ('name', 'city')


class HighEduAdmin(admin.ModelAdmin):

    list_display = ('worker', 'name', 'city', 'specialization', 'from_date', 'to_date', 'graduation_year')
    search_fields = ('name', 'city', 'specialization')


admin.site.register(WorkerSecondaryEducation, SecEduAdmin)
admin.site.register(WorkerHighEducation, HighEduAdmin)