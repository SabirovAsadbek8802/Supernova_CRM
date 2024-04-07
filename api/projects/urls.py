from django.urls import path
from .views import ProjectImagesViewset, ProjectViewset, TeamViewset, TaskViewset
from rest_framework import routers

router = routers.DefaultRouter()

# routes for project model
router.register(r'project', ProjectViewset)
router.register(r'task', TaskViewset)
router.register(r'team', TeamViewset)
router.register(r'project-images', ProjectImagesViewset)

urlpatterns = router.urls
