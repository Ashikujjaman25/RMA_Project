from django.db import models
from django.conf import settings

# Create your models here.
class Report(models.Model):
    STATUS_CHOICES = [
        ("DRAFT", "Draft"),
        ("SUBMITTED", "Submitted"),
    ]

    employee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reports",
    )

    title = models.CharField(max_length=200)

    report_date = models.DateField()

    work_done = models.TextField()

    work_plan = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="DRAFT",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-report_date", "-created_at"]

    def __str__(self):
        return f"{self.employee.username} - {self.report_date}"
