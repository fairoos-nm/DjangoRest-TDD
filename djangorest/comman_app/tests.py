from django.test import TestCase
from .models import Bucketlist
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


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

    def tearDown(self):
        """
        Remove test clinet after testing
        """
        Bucketlist.objects.get(name=self.bucklist_name).delete()


class ViewTestCase(TestCase):
    """
    Test suite for the common views
    """

    def setUp(self):
        """
        Define test clinent and other test varibale.
        """
        self.client = APIClient()
        self.bucketlist_data = {'name': 'Go to Canada'}
        self.response = self.client.post(reverse('create'),
                                         self.bucketlist_data,
                                         format='json')

    def test_api_can_ceate_bucketlist(self):
        """
        Test api has bucklist creation capability
        """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def tearDown(self):
        """
        Delete all created instance after testing
        """
        for key, value in self.bucketlist_data.items():
            Bucketlist.objects.get(key=value).delete()
