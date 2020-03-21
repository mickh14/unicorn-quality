from django import forms
from .models import Issue, Comment


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('name', 'description', 'status', 'step_to_Reproduce', 'expected_Results', 'actual_Results', 'issue_type')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')


class DoneForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('root_cause', 'resolution')
