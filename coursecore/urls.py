from django.urls import path
from .views import course
urlpatterns = [
    path("courses/", course, name="course_page")
]