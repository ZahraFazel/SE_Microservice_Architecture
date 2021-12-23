from django.db import models
from django.contrib.auth.models import User


class SystemAdmin(User):
    name = models.CharField(max_length=50)
    national_code = models.CharField(max_length=10, unique=True)

    class Meta:
        permissions = ()

    def __str__(self):
        return self.name
