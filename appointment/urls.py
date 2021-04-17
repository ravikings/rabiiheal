from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import UserList, UserDetail,AppointmentList, AppointmentDetail


urlpatterns = [
    path('users/', UserList.as_view()), 
    path('users/<int:pk>/', UserDetail.as_view()),
    path('<int:pk>/', AppointmentDetail.as_view()),
    path('', AppointmentList.as_view()),
]

