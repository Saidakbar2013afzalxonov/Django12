from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ('id', 'email', 'first_name', 'last_name', 'slug', 'phone_number')
    list_display_links = ('email',)
    list_editable = ('last_name',)

    list_filter = ('email',)
    list_per_page = 10

    search_fields = ('email', 'first_name', 'last_name')
    readonly_fields = ('slug',)

# Register your models here.

