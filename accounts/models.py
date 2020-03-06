from django.db import models

# Create your models here.


class User(models.Model):
    image = models.ImageField(upload_to="img", blank=True, null=True)

def __str__(self):
    return self.name    