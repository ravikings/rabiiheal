from django.db import models
from django.contrib.auth.models import User


class Appointment(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    symptom = models.CharField(max_length=250, blank=True)
    phone = models.IntegerField()
    dob = models.DateField()
    address = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=20, default='')
    state = models.CharField(max_length=10, default='')
    schedule_date = models.DateField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
