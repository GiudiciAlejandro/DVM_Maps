from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('start/', views.index, name="index"),
    path('create/', views.CameraCreateView.as_view(), name='create_camera'),
]
