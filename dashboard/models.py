from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):

    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4())
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, null=True)
    username = models.CharField(unique=True, max_length=100)
    email = models.CharField(unique=True, max_length=200)
    password = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user'
