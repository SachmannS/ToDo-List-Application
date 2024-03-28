from django.shortcuts import render
from rest_framework import viewsets
from .models import Task, TaskList 
from .serializers import TaskListSerializer, TaskSerializer
from rest_framework import generics


# Create your views here.
class TaskListViews(viewsets.ModelViewSet):
    serializer_class = TaskListSerializer
    
    def get_queryset(self):
        return TaskList.objects.filter(user = self.request.user)
    
    
class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     todo_id = self.request.query_params.get('todoId')
    #     if todo_id:
    #         queryset = queryset.filter(taskList=todo_id)
    #     return queryset
    
    # def destroy(self):
    #     queryset = self.queryset
    #     q = queryset.filter(id in [3,4])
    #     q.delete()

class Task(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

        
