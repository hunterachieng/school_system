from django.urls import path, include
from rest_framework import routers
from .views import StudentViewSet, TrainerViewSet,CourseViewSet,EventViewSet

router = routers.DefaultRouter()
router.register("students",StudentViewSet)
router.register("trainer", TrainerViewSet)
router.register("course", CourseViewSet)
router.register("event", EventViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("", include(router.urls)),
    path("", include(router.urls)),
    path("", include(router.urls))

]
