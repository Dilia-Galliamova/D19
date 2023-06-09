from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(
                        verbose_name='email',
                        max_length=255,
                        unique=True,
                    )
    username = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.username
