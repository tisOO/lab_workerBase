from django.contrib import admin

# Register your models here.
from .models import Department, DepartmentJobPosition, DepartmentReadOnlyProxy, DepartmentJobPositionReadonlyProxy

admin.site.register(Department, admin.ModelAdmin)
admin.site.register(DepartmentJobPosition, admin.ModelAdmin)


class DepartmentReadOnlyProxyAdmin(admin.ModelAdmin):
    readonly_fields = ['name', ]

admin.site.register(DepartmentReadOnlyProxy, DepartmentReadOnlyProxyAdmin)


class DepartmentJobPositionReadOnlyProxyAdmin(admin.ModelAdmin):
    readonly_fields = ['name', 'department']

admin.site.register(DepartmentJobPositionReadonlyProxy, DepartmentJobPositionReadOnlyProxyAdmin)

