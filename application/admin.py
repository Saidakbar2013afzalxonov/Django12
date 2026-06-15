from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserProfile
from . import models



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


admin.site.register(models.UserProfile)
admin.site.register(models.Post)
admin.site.register(models.Tag)
admin.site.register(models.Like)
admin.site.register(models.Comment)

# Register your models here.

