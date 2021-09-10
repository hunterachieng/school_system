from django.shortcuts import render
from course.models import Course


# Create your views here.

def course(request):
    courses = Course.objects.count()
    data ={"courses":courses}
    return render(request, "course_page.html", data)