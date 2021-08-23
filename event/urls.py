from django.conf.urls import url 
from .views import index, CalendarView, event
app_name = 'cal'
urlpatterns = [
    url(r'^index/$', index, name='index'),
    url(r'^cal/$', CalendarView.as_view(), name='calendar'),
    url(r'^event/new/$', event, name='event_new'),
	url(r'^event/edit/(?P<event_id>\d+)/$', event, name='event_edit'),
]