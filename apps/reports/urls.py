from django.urls import path

from . import views

urlpatterns = [
    path(
        "create/",
        views.create_report,
        name="create_report",
    ),

    path(
    "drafts/",
    views.draft_reports,
    name="draft_reports",
),

    path(
    "drafts/<int:report_id>/edit/",
    views.edit_draft,
    name="edit_draft",
),

path(
    "drafts/<int:report_id>/submit/",
    views.submit_report,
    name="submit_report",
),


path(
    "history/",
    views.report_history,
    name="report_history",
),
]