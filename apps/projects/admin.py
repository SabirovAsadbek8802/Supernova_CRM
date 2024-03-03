from django.contrib import admin
from .models import Project, ProjectImages, Task, Team

admin.site.register(Project)
admin.site.register(ProjectImages)
admin.site.register(Task)
admin.site.register(Team)