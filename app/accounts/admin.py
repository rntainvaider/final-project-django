from django.contrib import admin

from .models import (
    CustomUsers,
    ServiceOffices,
    WorkSchedule,
    UserRole,
    WorkScheduleDay,
    Receipt,
)


class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "full_name",
        "phone_number",
        "email",
        "password",
        "role",
    )
    list_display_links = (
        "full_name",
        "phone_number",
        "email",
    )


class WorkScheduleAdmin(admin.ModelAdmin):
    list_display = ("id", "service_office")
    list_display_links = ("id", "service_office")


class ServiceOfficesAdmin(admin.ModelAdmin):
    list_display = ("id", "address", "phone_numbers", "email_address")
    list_display_links = ("id", "address")


class WorkScheduleDayAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "work_schedule",
        "day_of_week",
        "start_time",
        "end_time",
        "is_off_day",
    )
    list_display_links = ("id", "work_schedule")


admin.site.register(CustomUsers, CustomUserAdmin)
admin.site.register(ServiceOffices, ServiceOfficesAdmin)
admin.site.register(WorkSchedule, WorkScheduleAdmin)
admin.site.register(UserRole)
admin.site.register(WorkScheduleDay, WorkScheduleDayAdmin)
admin.site.register(Receipt)
