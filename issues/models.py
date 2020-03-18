from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.


# Model for capturing components of an issue
class Issue(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    step_to_Reproduce = models.TextField(max_length=1000, default='')
    expected_Results = models.TextField(max_length=500, default='')
    actual_Results = models.TextField(max_length=500, default='')
    published_date = models.DateField(blank=True, null=True, default=timezone.now)
    issue_option = (
        ('Bug', 'Bug'),
        ('Feature', 'Feature'),
    )
    issue_type = models.CharField(max_length=30, blank=True, null=False, choices=issue_option)
    status_option = (
        ('Draft', 'Draft'),
        ('ToDo', 'ToDo'),
        ('InDevelopment', 'InDevelopment'),
        ('Fixed', 'Fixed'),
        ('InTest', 'InTest'),
    )
    status = models.CharField(max_length=30, blank=True, null=False, choices=status_option)
    views = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, default='5')
    name = models.CharField(max_length=254, default='')
    votes_required = models.IntegerField(default='100')
    root_cause = models.TextField(max_length=500, default='')
    resolution = models.TextField(max_length=500, default='')
    
    def __str__(self):
        return self.name


# Model for capturing components of an comment
class Comment(models.Model):
    Issue = models.ForeignKey(Issue, null=False)
    body = models.TextField(max_length=1000, default='')
    comment_date = models.DateField(blank=True, null=True, default=timezone.now)