from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

    class Meta:
        db_table = "User"
