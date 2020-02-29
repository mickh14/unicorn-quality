from django.shortcuts import render
from issues.models import Issue

# Create your views here.
from django.shortcuts import render
from issues.models import Issue

# Create your views here.
def do_search(request):
    issues = Issue.objects.filter(name__icontains=request.GET['q'])
    return render(request, "issues.html", {"issues": issues})