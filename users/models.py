from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import DateTimeField

class User(AbstractUser):
    last_activity = DateTimeField(blank=True, null=True)