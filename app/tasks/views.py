# Django rest Framework imports
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Models and serializers
from tasks.models import Task
from tasks.serializers import TaskSerializer


class BaseViewSet(viewsets.ModelViewSet):
    """Base viewset for user own attributes"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):
       """Return objects for the current authenticated user only"""
       assigned_only = bool(
           int(self.request.query_params.get('assigned_only', 0))
       )
       queryset = self.queryset
       if assigned_only:
           queryset = queryset.filter(recipe__isnull=False)
       return queryset.filter(user=self.request.user
                               ).order_by('-name').distinct()

    def perform_create(self, serializer):
        """Crete a new object"""
        serializer.save(user=self.request.user)
    

class TasksViewSet(BaseViewSet):
    """Tasks viewset"""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    def perform_create(self, serializer):
        """Create a new recipe"""
        serializer.save(user=self.request.user)