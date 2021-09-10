from django.shortcuts import render
from student.models import Student


# Create your views here.

def student(request):
    students = Student.objects.count()
    data ={"students":students}
    return render(request, "student_page.html", data)

