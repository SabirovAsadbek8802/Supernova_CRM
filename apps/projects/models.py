
from django.db import models
from apps.users.models import User

PRIORITIES = (
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('immediate', 'Immediate')
)

LEVELS = (
    ('easy', 'Easy'),
    ('medium', 'Medium'),
    ('hard', 'Hard')
)


class Project(models.Model):
    name = models.CharField(max_length=255)
    starts_at = models.DateField()
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=10, choices=PRIORITIES, default='low')
    description = models.TextField()
    level = models.CharField(max_length=10, choices=LEVELS, default='easy')
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_projects')
    assignees = models.ManyToManyField(User, related_name='projects_assignees')

    def __str__(self):
        return '%s - %s -%s' % (self.name, self.created_at, self.level)


class ProjectImages(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=255)
    task_group = models.CharField(max_length=255)
    estimate = models.DateField(null=True)
    deadline = models.DateField(null=True)
    priority = models.CharField(max_length=10, choices=PRIORITIES, default='low')
    status = models.BooleanField(default=False)
    description = models.TextField()
    assignees = models.ManyToManyField(User, related_name='tasks_assignees')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='user_tasks')

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='team_member')

    def __str__(self):
        return self.name
