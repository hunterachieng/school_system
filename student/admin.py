from django.contrib import admin
from .models import Student  #.models refers to the current directory

# Register your models here.
admin.site.register(Student)
