from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

from .forms import LoginForm


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