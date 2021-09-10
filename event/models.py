from django.db import models
from django.urls import reverse
from django.utils import timezone

class Event(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    description = models.TextField(null=True)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    venue=models.CharField(max_length=12,default="AkiraChix")


    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'