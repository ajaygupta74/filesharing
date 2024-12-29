from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User


class CustomUserAdmin(UserAdmin):
    model = User
    search_fields = ['email', 'email_confirmed', 'first_name', 'last_name',]
    list_filter = ('email_confirmed', 'is_staff', 'date_joined')
    ordering = ('-date_joined', )
    list_per_page = 25
    list_display = ['email', 'first_name', 'last_name', 'email_confirmed']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email_confirmed', 'date_joined')
        }),
        ('Permissions', {'fields': ('is_staff', 'user_permissions')}),
        ('Group Permissions', {'fields': ('groups', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )


admin.site.register(User, CustomUserAdmin)
