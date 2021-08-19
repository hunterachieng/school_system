from django.core.exceptions import RequestAborted
from django.shortcuts import render
from .forms import RegisterCourseForm
from .models import Course

# Create your views here.
def register_course(request):
    if request.method == "POST":
        form = RegisterCourseForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
         form = RegisterCourseForm()
    return render(request,"register_course.html",{"form":form})

#creating course list
def course_list(request):
    courses = Course.objects.all()
    return render(request,"course_list.html",{"courses":courses})

    
