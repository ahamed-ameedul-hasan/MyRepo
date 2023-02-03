from django.db import models

# Create your models here.
class register(models.Model):
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=25)