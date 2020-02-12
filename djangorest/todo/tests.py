from django.test import TestCase
from .models import Todo





class ModelTestCase(TestCase):
    """
    This class defines the test suite for the Todo model.
    """

    def setUp(self):
        """
        Define the client and other varibale
        """

        self.title = 'Plan 2020!'
        self.description = 'Go to Lendon'
        self.todo = Todo(title=self.title,
                         description=self.description)

    def test_model_can_create_todo(self):
        """
        Test todo model can create a todo list.
        """
        old_count = Todo.objects.count()
        self.todo.save()
        new_count = Todo.objects.count()
        self.assertNotEqual(old_count, new_count)
        
