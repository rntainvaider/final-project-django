from django.contrib import admin

from .models import CustomUsers, ServiceOffices, WorkSchedule, UserRole, WorkScheduleDay


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "phone_number", "email", "password", "role_id")
    list_display_links = ("id", "full_name", "phone_number", "email")


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
        "id",
        "address",
    )


class WorkScheduleAdmin(admin.ModelAdmin):
    list_display = ("id", "service_office")
    list_display_links = ("id", "service_office")


admin.site.register(CustomUsers, CustomUserAdmin)
admin.site.register(ServiceOffices, ServiceOfficesAdmin)
admin.site.register(WorkSchedule, WorkScheduleAdmin)
admin.site.register(UserRole)
admin.site.register(WorkScheduleDay)
