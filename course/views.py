from django.core.exceptions import RequestAborted
from django.shortcuts import redirect, render
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

def edit_course(request,id):
    course = Course.objects.get(id=id)
    if request.method == "POST":
        form = RegisterCourseForm(request.POST,instance=course)
        if form.is_valid():
            form.save()
    else:
        form=RegisterCourseForm(instance=course)
        return render(request,"edit_course.html",{"form":form})

def course_profile(request,id):
    course = Course.objects.get(id=id)
    return render(request,"course_profile.html", {"course":course})

def delete_course(request,id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect("course_list")

    
