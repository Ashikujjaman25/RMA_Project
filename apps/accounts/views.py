from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

from apps.core.decorators import role_required
from .forms import (
    LoginForm,
    DepartmentHeadCreationForm,
    EmployeeCreationForm,
)


def login_view(request):
    if request.user.is_authenticated:
        return redirect("/")

    form = LoginForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        return redirect("/")

    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("/accounts/login/")


class CustomPasswordChangeView(PasswordChangeView):
    template_name = "accounts/password_change.html"
    success_url = reverse_lazy("password_change_done")


# ==========================================
# Create Department Head (Admin Only)
# ==========================================

@role_required("ADMIN")
def create_department_head(request):

    form = DepartmentHeadCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():

        user = form.save(commit=False)
        user.role = "HEAD"
        user.set_password(form.cleaned_data["password"])
        user.save()

        return redirect("admin_dashboard")

    return render(
        request,
        "accounts/create_department_head.html",
        {
            "form": form,
        },
    )


# ==========================================
# Create Employee (Department Head Only)
# ==========================================

@role_required("HEAD")
def create_employee(request):

    form = EmployeeCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():

        user = form.save(commit=False)

        # Automatic Role
        user.role = "EMPLOYEE"

        # Employee belongs to Head's Department
        user.department = request.user.department

        # Hash Password
        user.set_password(form.cleaned_data["password"])

        user.save()

        return redirect("head_dashboard")

    return render(
        request,
        "accounts/create_employee.html",
        {
            "form": form,
        },
    )