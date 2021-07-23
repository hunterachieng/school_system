from django.shortcuts import render
from .forms import StudentRegistrationForm

# Create your views here.
# handles http requests
#class based and function based views

def register_student(request):
    #creating an instance of the form
    form = StudentRegistrationForm()
    return render(request,"register_student.html",{"form":form})

