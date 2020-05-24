from django.contrib import admin
from django.urls import path
from . import views

app_name = 'UNIV'


urlpatterns = [
    path('detail/',views.detail,name='detail'),
]