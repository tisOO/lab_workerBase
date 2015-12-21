from django.contrib import admin
from .models import WorkerSecondaryEducation, WorkerHighEducation
# Register your models here.

admin.site.register(WorkerHighEducation, admin.ModelAdmin)
admin.site.register(WorkerSecondaryEducation, admin.ModelAdmin)