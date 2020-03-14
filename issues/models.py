from django.db import models
from django.utils import timezone


# Create your models here.
from django.db import models


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
        ('Done', 'Done'),
    )
    status = models.CharField(max_length=30, blank=True, null=False, choices=status_option)
    views = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, default='5')
    name = models.CharField(max_length=254, default='')
    votes_required = models.IntegerField(default=0)
    

    def __str__(self):
        return self.name

class Comments(models.Model):
    Issue = models.ForeignKey(Issue, null=False)
    comments = models.TextField(max_length=1000, default='')