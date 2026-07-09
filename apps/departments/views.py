from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Department


@login_required(login_url="/accounts/login/")
def department_list(request):

    departments = Department.objects.all()

    return render(
        request,
        "departments/department_list.html",
        {
            "departments": departments
        }
    )