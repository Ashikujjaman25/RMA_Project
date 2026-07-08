from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.core.decorators import role_required


# ==========================
# Home (Role Based Redirect)
# ==========================

@login_required(login_url="/accounts/login/")
def home(request):
    if request.user.role == "ADMIN":
        return redirect("admin_dashboard")

    elif request.user.role == "HEAD":
        return redirect("head_dashboard")

    elif request.user.role == "EMPLOYEE":
        return redirect("employee_dashboard")

    return render(request, "core/home.html")


# ==========================
# Admin Dashboard
# ==========================

@login_required(login_url="/accounts/login/")
@role_required("ADMIN")
def admin_dashboard(request):
    return render(request, "core/admin_dashboard.html")


# ==========================
# Department Head Dashboard
# ==========================

@login_required(login_url="/accounts/login/")
@role_required("HEAD")
def head_dashboard(request):
    return render(request, "core/head_dashboard.html")


# ==========================
# Employee Dashboard
# ==========================

@login_required(login_url="/accounts/login/")
@role_required("EMPLOYEE")
def employee_dashboard(request):
    return render(request, "core/employee_dashboard.html")