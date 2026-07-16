from django import forms
from .models import Report


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = [
            "title",
            "report_date",
            "work_done",
            "work_plan",
        ]

        widgets = {
            "report_date": forms.DateInput(attrs={"type": "date"}),
            "work_done": forms.Textarea(attrs={"rows": 5}),
            "work_plan": forms.Textarea(attrs={"rows": 5}),
        }