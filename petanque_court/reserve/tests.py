from django.test import TestCase, Client
from django.urls import reverse
from reserve.models import Appointment
import json

# Create your tests here.
class TestViews(TestCase):
    def test_project_list_GET(self):
        client = Client()

        response = client.get(reverse('detail'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reserve/booking.html')