from django.db import models


class Bucketlist(models.Model):
    """
    This class defines the bucklist model.
    """
    name = models.CharField(max_length=225, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Return a human readable representation of the model instance
        """
        return '{}'.format(self.name)
