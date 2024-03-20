from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    is_superuser = None
    is_staff = None
    last_login = None
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4())
