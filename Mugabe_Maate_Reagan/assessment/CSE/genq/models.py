from django.db import models

# Create your models here.
class User_account(models.Model):
    
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=16)
    DOB=models.CharField(max_length=6)
    gender=models.CharField(max_length=6)
    LOCATION=models.CharField(max_length=16)
    state=models.CharField(max_length=20)
    vtown=models.CharField(max_length=10)
    icode=models.CharField(max_length=15)
    phone1=models.CharField(max_length=15)
    phone2=models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    