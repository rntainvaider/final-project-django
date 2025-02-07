from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class UserRole(models.Model):
    name = models.CharField(max_length=128, verbose_name="Наименование")

    class Meta:
        db_table = "users_role"
        verbose_name_plural = "Роли"
        verbose_name = "Роль"


class ServiceOffices(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=128, verbose_name="Адрес")
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Долгота")
    phone_numbers = models.CharField(max_length=18, verbose_name="Номер телефона")
    email_address = models.CharField(
        unique=True, max_length=128, verbose_name="Адрес электронной почты"
    )

    class Meta:
        db_table = "service_offices"
        verbose_name_plural = "Офисы обслуживания"
        verbose_name = "Офис обслуживания"


class CustomUsers(AbstractUser):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=55, verbose_name="ФИО")
    phone_number = models.CharField(max_length=18, verbose_name="Номер телефона")
    email = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128, verbose_name="Пароль")
    role = models.ForeignKey(
        UserRole, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Роль"
    )
    # service_office = models.ForeignKey(
    #     ServiceOffices,
    #     on_delete=models.PROTECT,
    #     null=False,
    #     verbose_name="Офис обслуживания",
    # )

    groups = models.ManyToManyField(Group, related_name="custom_users_groups")
    user_permissions = models.ManyToManyField(
        Permission, related_name="custom_users_permissions"
    )

    class Meta:
        db_table = "custom_user"
        verbose_name_plural = "Пользователи"
        verbose_name = "Пользователь"


class WorkSchedule(models.Model):
    id = models.AutoField(primary_key=True)
    days_of_week = models.CharField(max_length=128, verbose_name="День недели")
    start_time = models.TimeField(verbose_name="Время начала")
    end_time = models.TimeField(verbose_name="Время окончания")
    service_office = models.ForeignKey(
        ServiceOffices, on_delete=models.PROTECT, verbose_name="Офис обслуживания"
    )

    class Meta:
        db_table = "work_schedule"
        verbose_name_plural = "Графики работы"
        verbose_name = "График работы"
