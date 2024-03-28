from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TaskList(models.Model):
    name = models.CharField(max_length = 200, null = False)
    description = models.TextField(blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    dateCreated = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

class Task(models.Model):
    taskList = models.ForeignKey(TaskList, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200, null = False)
    description = models.TextField(blank = True)
    isCompleted = models.BooleanField(default = False)
    dateCreated = models.DateTimeField(auto_now_add = True)
    deadLine = models.DateTimeField(blank = True, null =True)

    def __str__(self):
        return self.name

