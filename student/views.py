from django.shortcuts import render
from .forms import StudentRegistrationForm

# Create your views here.
# handles http requests
#class based and function based views

#conducting form validation
def register_student(request):
    if request.method =="POST":
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else: 
         #creating an instance of the form

         form = StudentRegistrationForm()
    return render(request,"register_student.html",{"form":form})

