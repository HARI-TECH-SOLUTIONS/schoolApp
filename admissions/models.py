from django.db import models

# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=30)
    dob = models.DateField()
    fatherName = models.CharField(max_length=30)
    className = models.IntegerField()
    contact = models.CharField(max_length=15)
