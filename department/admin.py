from django.contrib import admin

# Register your models here.
from .models import Department, DepartmentJobPosition

admin.site.register(Department, admin.ModelAdmin)
admin.site.register(DepartmentJobPosition, admin.ModelAdmin)