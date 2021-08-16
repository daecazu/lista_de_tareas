"""test tasks model"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from tasks.models import Task
from tasks.serializers import TaskSerializer
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

TASKS_URL = reverse('task:task-list')


def sample_user(email='test@test.com', password='12345678'):
    """create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    """"""
    def test_task_str(self):
        """Test Task String Representation"""

        task = Task.objects.create(
            user=sample_user(),
            name='simple task',
            description='simple task description'
        )
        self.assertEqual(str(task), task.name)


class PublicApiTests(TestCase):
    """Test the publicly available Tasks API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required for retieving tasks"""

        res = self.client.get(TASKS_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTasksApiTests(TestCase):
    """Test the authorized user tasks API"""

    def setUp(self):
        self.user = sample_user()
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_tasks(self):
        """Test retrieving tasks"""
        Task.objects.create(user=self.user, name='My first task')
        Task.objects.create(user=self.user, name='My second task')

        res = self.client.get(TASKS_URL)

        tasks = Task.objects.all().order_by('-name')
        serializer = TaskSerializer(tasks, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_tasks_limited_to_user(self):
        """Test that tasks returned are for the authenticated user"""
        user2 = sample_user(
            'test2@test.com',
            '12345678'
        )
        Task.objects.create(
            user=user2,
            name='second user task',
            description='simple description'
        )
        task = Task.objects.create(
            user=self.user,
            name='loged user task',
            description='simple description'
        )

        res = self.client.get(TASKS_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], task.name)

    def test_create_task_sucessfull(self):
        """Test creating a new Task"""
        payload = {
            'name': 'Test Task!',
            'description': 'simple description'
        }
        res = self.client.post(TASKS_URL, payload)

        exists = Task.objects.filter(
            user=self.user,
            name=payload['name']
        ).exists()

        task = Task.objects.filter(
            user=self.user,
            name=payload['name']
        ).first()
        serializer = TaskSerializer(task)
        self.assertTrue(exists)
        self.assertEqual(res.data, serializer.data)

    def test_create_task_invalid(self):
        """Test creating a new task with invalid payload"""
        payload = {
            'name': ''
        }
        payload2 = {
            'name': 'Test task!',
            'description': ''
        } 
        res = self.client.post(TASKS_URL, payload)
        self.assertTrue(res.status_code, status.HTTP_400_BAD_REQUEST)
        res2 = self.client.post(TASKS_URL, payload2)
        self.assertTrue(res2.status_code, status.HTTP_400_BAD_REQUEST)
