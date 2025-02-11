from pyexpat import model
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUsers(AbstractUser):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=55, verbose_name="ФИО")
    phone_number = models.CharField(max_length=18, verbose_name="Номер телефона")
    email = models.CharField(max_length=125, unique=True)
    password = models.CharField(max_length=125, verbose_name="Пароль")
    role_id = models.IntegerField(default=1)

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
