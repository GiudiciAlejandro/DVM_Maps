from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('start/', views.Index.as_view(), name="Index"),
    path('create/', views.CameraCreateView.as_view(), name='create_camera'),
]
