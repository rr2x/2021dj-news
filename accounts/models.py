from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # null = db, blank = validation
    age = models.PositiveIntegerField(null=True, blank=True)
