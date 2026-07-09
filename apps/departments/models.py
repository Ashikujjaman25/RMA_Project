from django.db import models
from apps.accounts.models import CustomUser


class Department(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    code = models.CharField(
        max_length=20,
        unique=True
    )

    head = models.OneToOneField(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'role': 'HEAD'}
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name