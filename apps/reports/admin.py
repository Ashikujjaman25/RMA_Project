from django.contrib import admin
from .models import Report

# Register your models here.
@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "employee",
        "report_date",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "report_date",
    )

    search_fields = (
        "title",
        "employee__username",
    )

    ordering = (
        "-report_date",
        "-created_at",
    )
