from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Issue, Comment
from .forms import IssueForm, CommentForm, DoneForm

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

def increment_vote(request, pk):
    """
    Create a view that returns a single
    issue object based on the issue ID (pk) and
    render it to the 'issuedetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    issue_vote = get_object_or_404(Issue, pk=pk)
    issue_vote.votes += 1
    issue_vote.save()
    return redirect(issue_detail, issue_vote.pk)
    #return render(request, "issuedetail.html", {'issue_vote': issue_vote})

@login_required()
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


@login_required()
def add_comment(request, pk):
    """
    Create a view that allows us add a comment
    """
    issue = get_object_or_404(Issue, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES, instance=issue)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.issue = issue
            comment.save()
            return redirect(issue_detail, issue.pk)
    else:
        form = CommentForm(instance=issue)
    return render(request, 'commentform.html', {'form': form})


def pass_test(request, pk):
    """
    Create a view that allows us to enter details RCA and resolution for fixed/ developed issue
    """
    issue = get_object_or_404(Issue, pk=pk)
    if request.method == "POST":
        issue.status = "Done"
        form = DoneForm(request.POST, request.FILES, instance=issue)
        if form.is_valid():
            issue = form.save()
            return redirect(issue_detail, issue.pk)
    else:
        form = DoneForm(instance=issue)
    return render(request, 'doneform.html', {'form': form})