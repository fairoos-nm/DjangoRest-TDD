from rest_framework import generics, permissions
from .permissions import IsOwner
from .serializers import BucketlistSerializer, UserSerializer
from .models import Bucketlist, User

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner)

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save(owner=self.request.user)


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    This class handles the http GET, PUT and DELETE request
    """
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner)

class UserView(generics.ListAPIView):
    """View to list the user queryset."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailsView(generics.RetrieveAPIView):
    """View to retrieve a user instance."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreateView(generics.ListCreateAPIView):
    """
    This class defines to create user.
    """
    queryset = User.objects.all()
    
