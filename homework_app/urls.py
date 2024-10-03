from django.urls import path
from .views import TaskListView, TaskCreateView, task_stats

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/stats/', task_stats, name='task-stats'),
]
