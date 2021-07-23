from django import forms
from django.forms import fields
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    #telling the class which model the form is for
    class Meta:
        model = Student
        #MODEL ATTRIBUTES ARE FIELD FOR THE FORM
        #if you dont want all fields, input desired fields in a tuple ("first_name")
        fields = "__all__"
