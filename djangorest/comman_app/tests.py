from django.test import TestCase
from .models import Bucketlist


class ModelTestCase(TestCase):
    """
    This class defines the test suite for the Bucketlist model.
    """

    def setUp(self):
        """
        Define test client and other client varibale
        """
        self.bucklist_name = 'Write world class code'
        self.bucklist = Bucketlist(name=self.bucklist_name)

    def test_model_can_create_bucketlist(self):
        """
        Test bucklist model can create a bucklist
        """
        old_count = Bucketlist.objects.count()
        self.bucklist.save()
        new_count = Bucketlist.objects.count()
        self.assertNotEqual(old_count, new_count)
