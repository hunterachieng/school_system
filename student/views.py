from django.shortcuts import render
from .forms import StudentRegistrationForm
from .models import Student

# Create your views here.
# handles http requests
#class based and function based views

#conducting form validation
def register_student(request):
    if request.method =="POST":
        form = StudentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else: 
         #creating an instance of the form

         form = StudentRegistrationForm()
    return render(request,"register_student.html",{"form":form})

#lists all students
def student_list(request):
    students = Student.objects.all()
    return render(request,"student_list.html", {"students":students})

