from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account import models


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined',
                    'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username', 'name', 'surname')
    readonly_fields = ('id', 'date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    # readonly_fields = ('id', 'date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class TeacherAdmin(admin.ModelAdmin):
    list_display = ()
    search_fields = ()
    # readonly_fields = ('id', 'date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    # readonly_fields = ('id', 'date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(models.Account, AccountAdmin)
admin.site.register(models.School, SchoolAdmin)
admin.site.register(models.Teacher, TeacherAdmin)
admin.site.register(models.Student, StudentAdmin)
