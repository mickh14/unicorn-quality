from django.db import models
from django.utils import timezone

# Create your models here.
from django.db import models


# Model for capturing components of an issue
class Issue(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    issue_option = (
        ('Bug', 'Bug'),
        ('Feature', 'Feature'),
    )
    issue_type = models.CharField(max_length=30, blank=True, null=False, choices=issue_option)
    views = models.IntegerField(default=0)
    

    def __str__(self):
        return self.name