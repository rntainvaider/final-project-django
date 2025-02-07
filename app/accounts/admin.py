from django.contrib import admin

from .models import CustomUsers, ServiceOffices, UserRole, WorkSchedule


class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "full_name",
        "phone_number",
        "email",
        "password",
        "role_id",
    )
    list_display_links = (
        "full_name",
        "phone_number",
        "email",
    )


class ServiceOfficesAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "address",
        "latitude",
        "longitude",
        "phone_numbers",
        "email_address",
    )
    list_display_links = (
        "address",
        "phone_numbers",
        "email_address",
    )


admin.site.register(CustomUsers, CustomUserAdmin)
admin.site.register(ServiceOffices, ServiceOfficesAdmin)
admin.site.register(UserRole)
admin.site.register(WorkSchedule)
