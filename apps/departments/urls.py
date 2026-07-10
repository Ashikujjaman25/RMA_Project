from django.urls import path
from . import views


urlpatterns = [

    # Department List
    path(
        "",
        views.department_list,
        name="department_list"
    ),

    # Create Department
    path(
        "create/",
        views.create_department,
        name="create_department"
    ),

    # Edit Department
    path(
        "edit/<int:pk>/",
        views.edit_department,
        name="edit_department"
    ),

    # Delete Department
    path(
        "delete/<int:pk>/",
        views.delete_department,
        name="delete_department"
    ),

]