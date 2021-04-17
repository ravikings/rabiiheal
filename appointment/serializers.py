from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:

        fields = ('id', 'author', 'name', 'gender','symptom','phone','dob', 'address','city','state', 'schedule_date', 'created_at',)
        model = Appointment


class UserSerializer(serializers.ModelSerializer): 
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)