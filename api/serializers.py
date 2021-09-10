from django.db.models import fields
from rest_framework import serializers
from student.models import Student
from trainer.models import Trainer
from course.models import Course
from event.models import Event


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ("first_name", "last_name", "age")

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Trainer
        fields = ("first_name", "last_name", "email","course")

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("course_name","trainer", "course_description")

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

