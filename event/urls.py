from django.conf.urls import url
from django.urls import path
from .views import index, CalendarView, event,edit_event
app_name = 'cal'
urlpatterns = [
    url(r'^index/$', index, name='index'),
    url(r'^cal/$', CalendarView.as_view(), name='calendar'),
    url(r'^event/new/$', event, name='event_new'),
	url(r'^event/edit/(?P<event_id>\d+)/$', event, name='event_edit'),
    url("event/edit/<int:event_id>", edit_event, name='edit_event'),
]