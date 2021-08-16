# Django rest Framework imports
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from collections import OrderedDict
from rest_framework.pagination import PageNumberPagination
# Models and serializers
from tasks.models import Task
from tasks.serializers import TaskSerializer


class CustomPagination(PageNumberPagination):
    page_size = 20

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('current_page', self.page.number),
            ('pages', self.page.paginator.num_pages),
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data)
        ]))


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
        return queryset.filter(
                user=self.request.user.id
            ).order_by('-name').distinct()

    def perform_create(self, serializer):
        """Crete a new object"""
        serializer.save(user=self.request.user)


class TasksViewSet(BaseViewSet):
    """Tasks viewset"""
    search_fields = ['description']
    filter_backends = (filters.SearchFilter,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        """Create a new recipe"""
        serializer.save(user=self.request.user)
