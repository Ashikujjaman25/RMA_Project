from django.urls import path
from django.contrib.auth.views import (
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

from .views import (
    login_view,
    logout_view,
    CustomPasswordChangeView,
    create_department_head,
    create_employee,
    employee_list,
    edit_employee,
    delete_employee,
    view_employee,
)

urlpatterns = [
    # ==========================
    # Authentication
    # ==========================

    # Login
    path("login/", login_view, name="login"),

    # Logout
    path("logout/", logout_view, name="logout"),

    # ==========================
    # User Management
    # ==========================

    # Admin -> Create Department Head
    path(
        "create-department-head/",
        create_department_head,
        name="create_department_head",
    ),

    # Department Head -> Create Employee
    path(
        "create-employee/",
        create_employee,
        name="create_employee",
    ),

    # Department Head -> Employee List
    path(
        "employees/",
        employee_list,
        name="employee_list",
    ),

    # Department Head -> Edit Employee
    path(
        "employees/<int:user_id>/edit/",
        edit_employee,
        name="edit_employee",
    ),
    
    path(
    "employees/<int:user_id>/delete/",
    delete_employee,
    name="delete_employee",
    ) ,

    path(
    "employees/<int:user_id>/",
    view_employee,
    name="view_employee",
    ),

    # ==========================
    # Password Change
    # ==========================

    path(
        "password-change/",
        CustomPasswordChangeView.as_view(),
        name="password_change",
    ),

    path(
        "password-change/done/",
        PasswordChangeDoneView.as_view(
            template_name="accounts/password_change_done.html"
        ),
        name="password_change_done",
    ),

    # ==========================
    # Password Reset
    # ==========================

    path(
        "password-reset/",
        PasswordResetView.as_view(
            template_name="accounts/password_reset.html"
        ),
        name="password_reset",
    ),

    path(
        "password-reset/done/",
        PasswordResetDoneView.as_view(
            template_name="accounts/password_reset_done.html"
        ),
        name="password_reset_done",
    ),

    path(
        "reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="accounts/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),

    path(
        "reset/done/",
        PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]