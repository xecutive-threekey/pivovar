from django.contrib import admin
from account.models import MyUser, UserType
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea


class UserAdminConfig(UserAdmin):

    search_fields = ('email', 'username',)
    list_filter = ('email', 'username', 'is_staff')
    ordering = ('-date_joined',)
    list_display = ('email', 'username', 'date_joined', 'last_login',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'username',)}),
        ('Права', {'fields': ('user_type', 'is_superuser', 'is_staff', 'is_active')}),
    )

admin.site.register(MyUser, UserAdminConfig)
# admin.site.register(UserType)

