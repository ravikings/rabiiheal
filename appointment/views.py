from rest_framework import generics
from .models import Appointment
from .serializers import AppointmentSerializer


class AppointmentList(generics.ListCreateAPIView):

    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
