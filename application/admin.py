from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = (
         'username','id', 'email', 'first_name', 'last_name',
         'slug'
    )

    list_filter = ( 'is_superuser', 'is_staff', 'is_active')
    list_per_page = 10

    search_fields = ('username', 'email', 'first_name', 'last_name')

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'email',
                'password1',
                'password2',
                'first_name',
                'last_name',
            ),
        }),
    )

    readonly_fields = ('slug',)

admin.site.register(CustomUser, CustomUserAdmin)
# Register your models here.

