from rest_framework import serializers
from tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):
    """Serializer for tags objects"""

    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'status', 'priority')
        read_only_fields = ('id',)
    

