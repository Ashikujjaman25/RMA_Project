from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from .models import CustomUser

from apps.core.decorators import role_required
from .forms import (
    LoginForm,
    DepartmentHeadCreationForm,
    EmployeeCreationForm,
    EmployeeUpdateForm,
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

# ==========================================
# Employee List (Department Head Only)
# ==========================================

# ==========================================
# Employee List (Department Head Only)
# ==========================================

@role_required("HEAD")
def employee_list(request):

    search = request.GET.get("search", "").strip()

    employees = CustomUser.objects.filter(
        role="EMPLOYEE",
        department=request.user.department,
    )

    if search:
        employees = employees.filter(
            username__icontains=search
        )

    employees = employees.order_by(
        "first_name",
        "username",
    )

    paginator = Paginator(employees, 10)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "accounts/employee_list.html",
        {
            "page_obj": page_obj,
            "search": search,
        },
    )

# ==========================================
# Edit Employee (Department Head Only)
# ==========================================

@role_required("HEAD")
def edit_employee(request, user_id):

    employee = get_object_or_404(
        CustomUser,
        id=user_id,
        role="EMPLOYEE",
        department=request.user.department,
    )

    form = EmployeeUpdateForm(
        request.POST or None,
        instance=employee,
    )

    if request.method == "POST" and form.is_valid():

        form.save()

        return redirect("employee_list")

    return render(
        request,
        "accounts/edit_employee.html",
        {
            "form": form,
            "employee": employee,
        },
    )

# ==========================================
# Delete Employee (Department Head Only)
# ==========================================

@role_required("HEAD")
def delete_employee(request, user_id):

    employee = get_object_or_404(
        CustomUser,
        id=user_id,
        role="EMPLOYEE",
        department=request.user.department,
    )

    if request.method == "POST":

        employee.delete()

        return redirect("employee_list")

    return render(
        request,
        "accounts/delete_employee.html",
        {
            "employee": employee,
        },
    )