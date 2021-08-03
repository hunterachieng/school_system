from django.db import models

# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=30)
    event_date = models.DateField()
    description = models.TextField()
    venue = models.CharField(max_length=10)
    event_start= models.TimeField()
    event_end = models.TimeField()
    attendees = models.EmailField()
    event_link = models.URLField()
