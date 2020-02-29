from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Issue(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    steps_to_reproduce = models.TextField(max_length=140, default='Enter steps')
    expected_result = models.TextField(max_length=140, default='wWat should happen?')
    actual_result = models.TextField(max_length=140, default='What is happening?')
    

    def __str__(self):
        return self.name