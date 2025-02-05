from django.contrib import admin

from .models import CustomUsers


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "phone_number", "email", "password", "role_id")
    list_display_links = ("id", "full_name", "phone_number", "email")


admin.site.register(CustomUsers, CustomUserAdmin)
