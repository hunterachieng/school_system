from django.db import models
from django.forms.fields import CharField

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=20)
    gender_choice =((u'F',u'Female'),(u'M',u'Male'),(u'O',u'Others'))
    gender = models.CharField(max_length=10,choices=gender_choice)
    age = models.PositiveSmallIntegerField(default=None)
    date_of_birth = models.DateField(default=None)
    classes_name = models.CharField(max_length =10, default=None,null=True, blank=True)
    image = models.ImageField(default=None,upload_to= "images/")
    nationality_choice = ((u'K',u'Kenyan'),(u'U',u'Ugandan'),(u'R',u'Rwandan'),(u'S',u'Sudan'),(u'S',u'South Sudan'))
    nationality = models.CharField(max_length=10,choices=nationality_choice,default=None)
    national_id = models.CharField(max_length=20, default=None)
    email = models.EmailField(default=None)
    phone_number = models.CharField(max_length=14, default=None)
    medical_record = models.FileField(default=None, upload_to="files/")
    city =models.CharField(max_length=15, default=None)
    academic_year = models.BigIntegerField(default=None)
    guardian_name = models.CharField(max_length= 20, default=None)
    guardian_contact = models.CharField(max_length=14, default=None)
    admission_date = models.DateField(default=None)
    room_no = models.SmallIntegerField(default=None, null=True, blank=True)
    laptop_serial_number = models.CharField(max_length=20,null=True, blank=True)