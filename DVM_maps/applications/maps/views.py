from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from .forms import CameraModelForm
from .models import *
from bootstrap_modal_forms.generic import BSModalCreateView

class CameraCreateView(BSModalCreateView):
    template_name = 'newcamera.html'
    form_class = CameraModelForm
    success_message = 'Success: Camera was added.'
    success_url = reverse_lazy('index')


def index(request: HttpRequest) -> HttpResponse:
    return render(request,'./start.html' )