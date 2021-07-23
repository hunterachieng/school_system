from django.db import models
from django.forms.fields import CharField

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField(default=None)
    date_of_birth = models.DateField(default=None)
    classes_name = models.CharField(max_length =10, default=None)
    image = models.ImageField(default=None)
    national_id = models.CharField(max_length=20, default=None)
    email = models.CharField(max_length=30, default=None)
    phone_number = models.CharField(max_length=14, default=None)
    medical_record = models.FileField(default=None)
    gender = models.CharField(max_length=7, default=None)
    city =models.CharField(max_length=15, default=None)
    academic_year = models.DateField(default=None)
    guardian_name = models.CharField(max_length= 20, default=None)
    guardian_contact = models.CharField(max_length=14, default=None)
    admission_date = models.DateField(default=None)
    room_no = models.SmallIntegerField(default=None)