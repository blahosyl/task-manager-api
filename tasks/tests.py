from django.contrib.auth.models import User
from .models import Task
from rest_framework import status
from rest_framework.test import APITestCase


class TaskListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='adam', password='pass')

    def test_can_list_tasks(self):
        adam = User.objects.get(username='adam')
        Task.objects.create(owner=adam, title='a title')
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_task(self):
        self.client.login(username='adam', password='pass')
        response = self.client.post('/tasks/', {'title': 'a title'})
        count = Task.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_task(self):
        response = self.client.post('/tasks/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TaskDetailViewTests(APITestCase):
    def setUp(self):
        adam = User.objects.create_user(username='adam', password='pass')
        brian = User.objects.create_user(username='brian', password='pass')
        Task.objects.create(
            owner=adam, title='a title', description='adams description'
        )
        Task.objects.create(
            owner=brian, title='another title', description='brians description'
        )

    def test_can_retrieve_task_using_valid_id(self):
        response = self.client.get('/tasks/1/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_task_using_invalid_id(self):
        response = self.client.get('/tasks/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_task(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put('/tasks/1/', {'title': 'a new title'})
        task = Task.objects.filter(pk=1).first()
        self.assertEqual(task.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_task(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put('/tasks/2/', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)