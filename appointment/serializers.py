from rest_framework import serializers
from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:

        fields = ('id', 'author', 'name', 'gender','symptom','phone','dob', 'address','city','state', 'schedule_date', 'created_at',)
        model = Appointment
