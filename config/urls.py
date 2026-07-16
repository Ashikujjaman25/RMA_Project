from django.contrib import admin
from django.urls import path, include
from apps.core import views

urlpatterns = [
    # Home (Role Based Redirect)
    path("", views.home, name="home"),

    # Django Admin
    path("admin/", admin.site.urls),

    # Accounts
    path("accounts/", include("apps.accounts.urls")),

    # Departments
    path("departments/", include("apps.departments.urls")),

    # Reports
    path("reports/", include("apps.reports.urls")),

    # Dashboards
    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("head-dashboard/", views.head_dashboard, name="head_dashboard"),
    path("employee-dashboard/", views.employee_dashboard, name="employee_dashboard"),
]