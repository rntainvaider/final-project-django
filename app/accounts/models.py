from django.db import models


class CustomUsers(models.Model):
    full_name = models.CharField(max_length=55)
    phone_number = models.CharField(max_length=18)
    email = models.CharField(max_length=125)
    password = models.CharField(max_length=125)
    role_id = models.IntegerField(default=1)

    class Meta:
        db_table = "custom_user"
