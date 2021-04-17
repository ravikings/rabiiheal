from rest_framework import generics, viewsets
from django.contrib.auth import get_user_model
from .models import Appointment
from .permissions import IsAuthorOrReadOnly
from .serializers import AppointmentSerializer, UserSerializer


class AppointmentList(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class UserList(generics.ListCreateAPIView): 
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    

class UserDetail(generics.RetrieveUpdateDestroyAPIView): 
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

