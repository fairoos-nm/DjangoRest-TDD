from .serializers import TodoSerializer
from .models import Todo
from rest_framework import generics


class CreateView(generics.ListCreateAPIView):
    """
    This class define the create behaviour of api view
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        """
        Save the post data when creating a new bucketlist.
        """
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    This class define the PUT, GET and DELETE behaviour of the api view
    """
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    



