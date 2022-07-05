from sys import implementation
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account

class AccountAdmin(UserAdmin):
    list_display = ('email', 'rollno', 'first_name', 'last_name', 'phone', 'is_admin', 'is_staff', 'is_alloted', 'room_no')

    add_fieldsets = (
        (None, {'fields': ('rollno', 'email', 'password', 'first_name', 'last_name', 'phone', 'date_joined', 'last_login', 'is_admin', 'is_active', 'is_staff', 'is_superuser', 'is_alloted', 'room_no')}),
    )

    fieldsets = (
        (None, {
            "fields": (
                ('rollno', 'email', 'password', 'first_name', 'last_name', 'phone', 'date_joined', 'last_login', 'is_admin', 'is_active', 'is_staff', 'is_superuser', 'is_alloted', 'room_no')
                
            ),
        }),
    )

    search_fields = ('rollno', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    ordering = ()

admin.site.register(Account, AccountAdmin)

# admin.site.register(Account)