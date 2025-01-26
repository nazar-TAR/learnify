from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True, null=True)
    bio = models.TextField(blank=True)
    is_author = models.BooleanField(default=False)

    def __str__(self):
        return self.username
