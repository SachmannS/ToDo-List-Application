from rest_framework.routers import DefaultRouter
from .views import TaskListViews, TaskView, Task
from django.urls import path

router = DefaultRouter()
router.register('list', TaskListViews, basename = "task list")
router.register('tasks', TaskView, basename = "task")

urlpatterns = router.urls + [
    path("taskss/<int:pk>/", Task.as_view(), name = "something")
]