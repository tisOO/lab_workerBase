from django.contrib import admin

# Register your models here.
from .models import Worker, WorkerChild, JobPosition

admin.site.register(Worker, admin.ModelAdmin)
admin.site.register(WorkerChild, admin.ModelAdmin)
admin.site.register(JobPosition, admin.ModelAdmin)