from rest_framework import generics, filters
from homework_app.models.task import Task
from homework_app.serializers.task import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from django.utils import timezone


class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskPagination(PageNumberPagination):
    page_size = 10


class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['status', 'deadline']
    ordering_fields = ['deadline']
    ordering = ['deadline']
    pagination_class = TaskPagination


@api_view(['GET'])
def task_stats(request):
    total_tasks = Task.objects.count()
    status_count = Task.objects.values('status').annotate(count=Count('id'))
    overdue_tasks = Task.objects.filter(
        deadline__lt=timezone.now(), status__in=['pending', 'in_progress']
    ).count()

    stats = {
        'total_tasks': total_tasks,
        'status_count': status_count,
        'overdue_tasks': overdue_tasks
    }
    return Response(stats)