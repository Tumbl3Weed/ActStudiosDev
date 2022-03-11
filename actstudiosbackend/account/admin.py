from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account import models


admin.site.register(models.Account)
admin.site.register(models.School)
admin.site.register(models.Teacher)
admin.site.register(models.Student)
admin.site.register(models.Attendance)
admin.site.register(models.Note)
