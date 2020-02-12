from django.test import TestCase
from .models import Todo
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User





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

class ViewTestCase(TestCase):
    """
    Test suit for the todo view
    """

    def setUp(self):
        """
        Define test clinent and other test varibale.
        """
        user = User.objects.create(username='razi')
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        self.todo_data = {'title' : 'plan 2020!',
                          'description' : 'Go to Canada'}
        self.response = self.client.post(reverse('create'),
                                         self.todo_data,
                                         format="json")
        self.todolist = Todo.objects.get(
            title=list(self.todo_data.values())[0])

    def test_api_can_ceate_todo(self):
        """
        Test api has todo creation capability
        """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        
    def test_api_can_get_a_todo(self):
        """
        Test the api can get an given todo.
        """
        response = self.client.get(reverse('details',
                                           kwargs={'pk': self.todolist.id}),
                                   format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.todolist)

    def test_api_can_update_a_todo(self):
        """
        Test the api can  updata a given todo
        """

        new_data = {'description': 'Test description'}
        response = self.client.put(
            reverse('details',
                    kwargs={'pk': self.todolist.id}),
            new_data,
            format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_a_todo(self):
        """
        Test the api can delete a given instance.
        """

        response = self.client.delete(
            reverse('details',
                    kwargs={'pk': self.todolist.id}),
            format="json",
            follow=True)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
