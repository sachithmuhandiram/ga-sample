from django.test import TestCase, Client
from django.urls import reverse


class CreateActivityViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_an_activity(self):
        url = reverse("course_module:create_an_activity")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # Add more assertions as needed
