from django.db import models

# Create your models here.

#Creating company model
class Company(models.Model):
    # company_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, primary_key=True)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100,choices=(('Non IT','Non IT'),('IT','IT'),('Mobile Phones','Mobile Phones')))
    added_date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)
