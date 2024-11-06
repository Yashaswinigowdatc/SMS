# sms/urls.py

from django.urls import path
from . import views

app_name = 'sms'

urlpatterns = [
    path('', views.send_sms, name='send_sms'),
    path('success/', views.success, name='success'),
]
