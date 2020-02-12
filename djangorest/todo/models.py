from django.db import models

class Todo(models.Model):
    """
    This class define Todo model.
    """
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    
    def _str_(self):
        return self.title
