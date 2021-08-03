from django import forms
from django.forms import fields
from .models import Course

class RegisterCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"