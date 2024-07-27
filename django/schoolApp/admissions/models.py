from django.db import models

# Create your models here.
class StudentAdmissionModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')])
