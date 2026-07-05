from django.urls import path
from django.contrib.auth.views import PasswordChangeDoneView

from .views import (
    login_view,
    logout_view,
    CustomPasswordChangeView,
)

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),

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
]