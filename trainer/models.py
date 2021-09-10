from django.db import models

# Create your models here.
class Trainer (models.Model):
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=20)
    image = models.ImageField(default=None,upload_to= "images/", null=True)
    email = models.EmailField(default=None)
    phone_number = models.CharField(max_length=14, default=None , null=True)
    national_id = models.CharField(max_length=20, default=None, null=True)
    gender_choice =((u'F',u'Female'),(u'M',u'Male'),(u'O',u'Others'))
    gender = models.CharField(max_length=10,choices=gender_choice)
    city = models.CharField(max_length=10, null=True)
    company = models.CharField(max_length=30, null=True)
    course = models.CharField(max_length=20, null=True)    
    contract = models.FileField(upload_to="files/", null=True)
    resume = models.FileField(upload_to="files/", null=True)
    salary = models.BigIntegerField(null=True)
