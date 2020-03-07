from django import forms
from .models import Issue

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('name', 'description', 'status', 'step_to_Reproduce', 'expected_Results', 'actual_Results', 'issue_type', 'published_date')