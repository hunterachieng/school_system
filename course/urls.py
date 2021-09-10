from django.urls import path
from .views import register_course,course_list,edit_course,course_profile,delete_course

urlpatterns = [
    path("register/", register_course, name="register_course"),
    path("list/",course_list,name="course_list"),
    path("edit/<int:id>/", edit_course, name="edit_course"),
    path("profile/<int:id>/", course_profile, name="course_profile"),
    path("delete/<int:id>/", delete_course, name="delete_course"),
]