from django.shortcuts import redirect, render
from django.contrib.auth import login
from .forms import LoginForm
from django.contrib.auth import login, logout


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