from django.shortcuts import render
from issues.models import Issue
from django.contrib import messages

# Create your views here.
# Filter issue based on name


def do_search(request):
    issues = Issue.objects.filter(name__icontains=request.GET['q'])
    if issues == None:
        messages.error(request, "There were no results")
    else:    
        return render(request, "issues.html", {"issues": issues})


    # Filter issue based on bug
def issue_filter(request):
    issues = Issue.objects.filter(issue_type__icontains=request.GET['b'])
    return render(request, "issues.html", {"issues": issues})


def bug_done(request):
    status = Issue.objects.filter(status__exact='Done').filter(issue_type__exact='Bug')
    return render(request, "developed.html", {"issues": status})


def feature_done(request):
    status = Issue.objects.filter(status__exact='Done').filter(issue_type__exact='Feature')
    return render(request, "developed.html", {"issues": status})      