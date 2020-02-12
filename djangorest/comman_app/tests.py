from django.test import TestCase
from .models import Bucketlist
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User


class ModelTestCase(TestCase):
    """
    This class defines the test suite for the Bucketlist model.
    """

    def setUp(self):
        """
        Define test client and other client varibale
        """
        user = User.objects.create(username='razi')
        self.bucklist_name = 'Write world class code'
        self.bucklist = Bucketlist(name=self.bucklist_name, owner=user)

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
        user = User.objects.create(username='razi')
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        self.bucketlist_data = {'name': 'Go to Canada', 'owner': user.id}
        self.response = self.client.post(reverse('create'),
                                         self.bucketlist_data,
                                         format="json")
        self.bucketlist = Bucketlist.objects.get(
            name=list(self.bucketlist_data.values())[0])

    def test_api_can_ceate_bucketlist(self):
        """
        Test api has bucklist creation capability
        """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_bucketlist(self):
        """
        Test the api can get an given bucketlist.
        """
        response = self.client.get(reverse('details',
                                           kwargs={'pk': self.bucketlist.id}),
                                   format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.bucketlist)

    def test_api_can_update_a_bucketlist(self):
        """
        Test the api can  updata a given bucketlist
        """

        new_data = {'name': 'Back to India'}
        response = self.client.put(
            reverse('details',
                    kwargs={'pk': self.bucketlist.id}),
            new_data,
            format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_a_bucketlist(self):
        """
        Test the api can delete a given instance.
        """

        response = self.client.delete(
            reverse('details',
                    kwargs={'pk': self.bucketlist.id}),
            format="json",
            follow=True)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # def tearDown(self):
    #     """
    #     Delete all created instance after testing
    #     """
    #     for value in self.bucketlist_data.values():
    #         Bucketlist.objects.get(name=value).delete()
