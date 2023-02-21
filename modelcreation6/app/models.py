from django.db import models

# Create your models here.

class Persons(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone=models.IntegerField(null=True)
    joindate=models.DateField(null=True)