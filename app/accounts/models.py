from django.db import models


class CustomUsers(models.Model):
    name = models.CharField(max_length=55)
