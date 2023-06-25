from django.db import models

# Create your models here.
class Paziresh(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=500)
    school_name = models.CharField(max_length=500)
    grade = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    parent_phone = models.CharField(max_length=20)
    group_name = models.CharField(max_length=50)
    created_bey = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now=True)