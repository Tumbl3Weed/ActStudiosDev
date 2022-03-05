from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from api.models import Account


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username','date_joined','last_login','is_admin','is_staff')
    search_fields = ('email','username','name','surname')
    readonly_fields = ('id','date_joined','last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(Account, AccountAdmin)
# Register your models here.
