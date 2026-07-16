from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import ReportForm
from .models import Report
from django.db.models import Q

# Create your views here.
@login_required
def create_report(request):
    if request.method == "POST":
        form = ReportForm(request.POST)

        if form.is_valid():
            report = form.save(commit=False)
            report.employee = request.user
            report.save()

            return redirect("employee_dashboard")

    else:
        form = ReportForm()

    return render(
        request,
        "reports/create_report.html",
        {
            "form": form,
        },
    )

@login_required
def draft_reports(request):
    drafts = Report.objects.filter(
        employee=request.user,
        status="DRAFT",
    )

    return render(
        request,
        "reports/draft_reports.html",
        {
            "drafts": drafts,
        },
    )


@login_required
def edit_draft(request, report_id):
    report = get_object_or_404(
        Report,
        id=report_id,
        employee=request.user,
        status="DRAFT",
    )

    if request.method == "POST":
        form = ReportForm(request.POST, instance=report)

        if form.is_valid():
            form.save()
            return redirect("draft_reports")

    else:
        form = ReportForm(instance=report)

    return render(
        request,
        "reports/edit_draft.html",
        {
            "form": form,
            "report": report,
        },
    )


@login_required
def submit_report(request, report_id):
    if request.method != "POST":
        return redirect("draft_reports")

    report = get_object_or_404(
        Report,
        id=report_id,
        employee=request.user,
        status="DRAFT",
    )

    report.status = "SUBMITTED"
    report.save(update_fields=["status"])

    return redirect("draft_reports")


@login_required
def report_history(request):
    reports = Report.objects.filter(
        employee=request.user,
        status="SUBMITTED",
    )

    title = request.GET.get("title", "").strip()
    report_date = request.GET.get("report_date", "").strip()

    if title:
        reports = reports.filter(title__icontains=title)

    if report_date:
        reports = reports.filter(report_date=report_date)

    return render(
        request,
        "reports/report_history.html",
        {
            "reports": reports,
            "title": title,
            "report_date": report_date,
        },
    )
 