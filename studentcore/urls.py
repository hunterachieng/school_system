from django.urls import path
from .views import student
urlpatterns = [
    path("students/", student, name="student_page")
]