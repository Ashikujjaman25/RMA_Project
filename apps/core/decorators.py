from functools import wraps
from django.shortcuts import redirect


def role_required(*allowed_roles):
    """
    Custom RBAC Decorator

    Example:
    @role_required("ADMIN")
    @role_required("HEAD")
    @role_required("ADMIN", "HEAD")
    """

    def decorator(view_func):

        @wraps(view_func)
        def wrapper(request, *args, **kwargs):

            # User must be logged in
            if not request.user.is_authenticated:
                return redirect("/accounts/login/")

            # Role Allowed
            if request.user.role in allowed_roles:
                return view_func(request, *args, **kwargs)

            # Redirect based on role
            if request.user.role == "ADMIN":
                return redirect("admin_dashboard")

            elif request.user.role == "HEAD":
                return redirect("head_dashboard")

            elif request.user.role == "EMPLOYEE":
                return redirect("employee_dashboard")

            # Fallback
            return redirect("/accounts/login/")

        return wrapper

    return decorator