from django.urls import path
from .views import trainer
urlpatterns = [
    path("trainers/", trainer, name="trainer_page")
]