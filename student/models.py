from django.db import models
from django.forms.fields import CharField

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=20)
    gender_choice =((u'F',u'Female'),(u'M',u'Male'),(u'O',u'Others'))
    gender = models.CharField(max_length=10,choices=gender_choice)
    age = models.PositiveSmallIntegerField(default=None)
    date_of_birth = models.DateField(default=None, null=True)
    classes_name = models.CharField(max_length =10, default=None,null=True, blank=True)
    image = models.ImageField(default=None,upload_to= "images/")
    nationality_choice = ((u'K',u'Kenyan'),(u'U',u'Ugandan'),(u'R',u'Rwandan'),(u'S',u'Sudan'),(u'S',u'South Sudan'))
    nationality = models.CharField(max_length=10,choices=nationality_choice,default=None, null=True)
    national_id = models.CharField(max_length=20, default=None, null=True)
    email = models.EmailField(default=None,null=True)
    phone_number = models.CharField(max_length=14, default=None,null=True)
    medical_record = models.FileField(default=None, upload_to="files/", null=True)
    city =models.CharField(max_length=15, default=None, null=True)
    academic_year = models.IntegerField(default=None, null=True)
    guardian_name = models.CharField(max_length= 20, default=None, null=True)
    guardian_contact = models.CharField(max_length=14, default=None, null=True)
    admission_date = models.DateField(default=None, null=True)
    room_no = models.SmallIntegerField(default=None, null=True, blank=True)
    laptop_serial_number = models.CharField(max_length=20,null=True, blank=True)