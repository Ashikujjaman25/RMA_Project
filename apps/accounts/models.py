from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ("ADMIN", "Administration"),
        ("HEAD", "Department Head"),
        ("EMPLOYEE", "Employee"),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="EMPLOYEE",
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )

    # Department Assignment
    department = models.ForeignKey(
        "departments.Department",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="employees",
    )

    def __str__(self):
        return self.username