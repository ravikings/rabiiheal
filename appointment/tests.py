import json 
from json import JSONDecoder
from unittest.result import TestResult

from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase, Client
from django.http import HttpRequest, request, HttpResponse
from django.http import JsonResponse

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework import response, serializers
from rest_framework.authtoken.models import Token
from rest_framework.fields import SerializerMethodField
from rest_framework.response import Response
from django.urls import include, path, reverse
from rest_framework.test import APIClient, RequestsClient
from rest_framework.test import APITestCase, URLPatternsTestCase, APIRequestFactory

from appointment.serializers import UserSerializer
from appointment.models import Appointment
from .views import AppointmentList
from appointment.models import Appointment

# Create your tests here.


# http://127.0.0.1:8000/api/v1/dj-rest-auth/login/.
# http://127.0.0.1:8000/api/v1/dj-rest-auth/logout/.
# http://127.0.0.1:8000/api/v1/dj-rest-auth/password/reset
# http://127.0.0.1:8000/api/v1/dj-rest-auth/password/reset


class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {"username": "testcase", "email": "test@gmail.com",
                "password1": "123test4@", "password2": "123test4@"
                }
        response = self.client.post("/api/v1/dj-rest-auth/registration/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unauthorize_login_view(self):
        # data = {
        #     "detail": "Authentication credentials were not provided."
        # }

        response = self.client.get("/api/v1/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_login_for_register_user(self):
        data = {
            "Username": "admin",
            "Password": "admin"
        }
        response = self.client.post("/api-auth/login/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_appiontment_schedule_data(self):

        data = {
            "Username": "admin",
            "Password": "admin"
        }

        response = self.client.post("/api-auth/login/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_appiontment_schedule_data_for_authorized_user(self):

        c = Client()
        c.login(username='admin', password='admin')
        response = c.get("/api/v1/1")
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response['content-type'], 'text/html; charset=utf-8')

    def test_unauthorization_denial_access_for_appiontment_list(self):
        factory = APIRequestFactory()
        view = AppointmentList.as_view()
        request = factory.get('/api/v1/1')
        response = view(request, pk='1')
        response.render()
        self.assertEqual(response.content.decode(
            'utf-8'), '{"detail":"Authentication credentials were not provided."}')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authorization_access_for_appiontment_list(self):
        data = {
            "Username": "admin",
            "Password": "admin"
        }

        response = self.client.post("/api-auth/login/", data, content_type='application/json')
        html = response.content.decode('utf8')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('<label for="id_password">Password:</label>', html)
     
