from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Issue
from .forms import IssueForm

# Create your views here.
def all_issues(request):
    issues = Issue.objects.all()
    return render(request, "issues.html", {"issues": issues})

def all_bugs(request):
    bugs = Issue.objects.filter(issue_type__icontains="Bug")
    return render(request, "bugs.html", {"bugs": bugs})

def issue_detail(request, pk):
    """
    Create a view that returns a single
    issue object based on the issue ID (pk) and
    render it to the 'issuedetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    issue = get_object_or_404(Issue, pk=pk)
    issue.views += 1
    issue.save()
    return render(request, "issuedetail.html", {'issue': issue})

def create_or_edit_issue(request, pk=None):
    """
    Create a view that allows us to create
    or edit an issue depending if the issue ID
    is null or not
    """
    issue = get_object_or_404(Issue, pk=pk) if pk else None
    if request.method == "POST":
        form = IssueForm(request.POST, request.FILES, instance=issue)
        if form.is_valid():
            issue = form.save()
            return redirect(issue_detail, issue.pk)
    else:
        form = IssueForm(instance=issue)
    return render(request, 'issueform.html', {'form': form})