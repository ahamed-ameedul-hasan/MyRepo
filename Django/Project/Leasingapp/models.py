from django.db import models

# Create your models here.
class uploadfile(models.Model):
    Name = models.CharField(max_length=85)
    Description = models.CharField(max_length=100)
    Price = models.CharField(max_length=25)
    Picture = models.FileField()
    Status = models.BooleanField(default=False)

class register(models.Model):
    Name = models.CharField(max_length=35)
    Address = models.CharField(max_length=70)
    Days = models.CharField(max_length=15)
    Mobile = models.CharField(max_length=12)
    Email = models.CharField(max_length=50)
    Aadhar = models.CharField(max_length=15)
    Status = models.BooleanField(default=False)

class user(models.Model):
    Name = models.CharField(max_length=35)
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=20)
    Address = models.CharField(max_length=70)
    Status = models.BooleanField(default=False)

class adder(models.Model):
    Name = models.CharField(max_length=35)
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=20)
    Address = models.CharField(max_length=70)
    Status = models.BooleanField(default=False)

