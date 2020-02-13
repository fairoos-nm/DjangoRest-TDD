from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    """
    serializer to  map the modle instance in to JSON
    """
    class Meta:
        """
        Meta class to map serializer's fields with the model fields.
        """
        model = Todo
        fields = ('id', 'title', 'description', 'completed')
        
    
    
    
