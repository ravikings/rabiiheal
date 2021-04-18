import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
#from .models import Appointment


client = Client()

class GetAllPuppiesTest(TestCase):

    def test_get_all_puppies(self):
        response = client.get(reverse('/api/v1/'))
        #data = Appointment.objects.all()
        self.assertEqual(response.status_code, status.HTTP_200_OK)