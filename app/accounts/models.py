from django.db import models


class CustomUsers(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=55, verbose_name="ФИО")
    phone_number = models.CharField(max_length=18, verbose_name="Номер телефона")
    email = models.CharField(max_length=125, unique=True)
    password = models.CharField(max_length=125, verbose_name="Пароль")
    role_id = models.IntegerField(default=1)

    class Meta:
        db_table = "custom_user"
        verbose_name_plural = "Пользователи"
        verbose_name = "Пользователь"
