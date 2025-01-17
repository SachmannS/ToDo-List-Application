from rest_framework import serializers
from .models import TaskList, Task

class TaskListSerializer(serializers.ModelSerializer):
    class Meta :
        model = TaskList
        fields = ['id', 'name', 'user', 'dateCreated']


class TaskSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Task
        fields = '__all__'

