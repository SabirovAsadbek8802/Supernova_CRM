from .serializers import *
from rest_framework import viewsets
from .models import Project, ProjectImages, Task, Team


class ProjectViewset(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
class ProjectImagesViewset(viewsets.ModelViewSet):
    queryset = ProjectImages.objects.all()
    serializer_class = ProjectImagesSerializer
    
class TaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TasksSerializer
    
class TeamViewset(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer