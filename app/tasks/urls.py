from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import TasksViewSet

app_name = 'task'

router = DefaultRouter()
router.register('tasks', TasksViewSet)

urlpatterns = [
    path('', include(router.urls))
]