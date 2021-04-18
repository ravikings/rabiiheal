import json
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
from rest_framework.test import APITestCase, URLPatternsTestCase

from appointment.serializers import UserSerializer
from appointment.models import Appointment
from .views import AppointmentList

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


x=RegistrationTestCase()
print(x.test_appiontment_schedule_data_for_authorized_user())

