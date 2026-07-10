from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from apps.core.decorators import role_required

from .models import Department
from .forms import DepartmentForm


# ==========================
# Department List
# ==========================

@login_required(login_url="/accounts/login/")
def department_list(request):

    departments = Department.objects.all().order_by("id")

    return render(
        request,
        "departments/department_list.html",
        {
            "departments": departments
        }
    )


# ==========================
# Create Department
# ==========================

@login_required(login_url="/accounts/login/")
@role_required("ADMIN")
def create_department(request):

    if request.method == "POST":

        form = DepartmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("department_list")

    else:

        form = DepartmentForm()

    return render(
        request,
        "departments/create_department.html",
        {
            "form": form
        }
    )


# ==========================
# Edit Department
# ==========================

@login_required(login_url="/accounts/login/")
@role_required("ADMIN")
def edit_department(request, pk):

    department = get_object_or_404(
        Department,
        pk=pk
    )

    if request.method == "POST":

        form = DepartmentForm(
            request.POST,
            instance=department
        )

        if form.is_valid():
            form.save()
            return redirect("department_list")

    else:

        form = DepartmentForm(
            instance=department
        )

    return render(
        request,
        "departments/edit_department.html",
        {
            "form": form,
            "department": department
        }
    )


# ==========================
# Delete Department
# ==========================

@login_required(login_url="/accounts/login/")
@role_required("ADMIN")
def delete_department(request, pk):

    department = get_object_or_404(
        Department,
        pk=pk
    )

    if request.method == "POST":

        department.delete()

        return redirect("department_list")

    return render(
        request,
        "departments/delete_department.html",
        {
            "department": department
        }
    )