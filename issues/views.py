from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Issue

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
    issue object based on the post ID (pk) and
    render it to the 'issuedetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    issue = get_object_or_404(Issue, pk=pk)
    issue.views += 1
    issue.save()
    return render(request, "issuedetail.html", {'issue': issue})