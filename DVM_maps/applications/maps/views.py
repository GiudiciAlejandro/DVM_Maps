from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from .forms import CameraModelForm
from .models import *
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalReadView, BSModalDeleteView


class Index(generic.ListView):
    model = Camera
    context_object_name = 'camera'
    template_name = 'start.html'


#Create camera
class CameraCreateView(BSModalCreateView):
    template_name = 'newcamera.html'
    form_class = CameraModelForm
    success_message = 'Success: Camera was added.'    

    def form_valid(self, form):
       site_instance = Site.objects.get(pk=1)
       siteform = form.save(commit = False)
       siteform.site = site_instance
       response = super().form_valid(form)
       return response
       siteform.save()

    def get_success_url(self):
        return reverse_lazy('Index')

    # def Index(request: HttpRequest) -> HttpResponse:
    #     return render(request,'./start.html' )
    
    

# Update camera
class BookUpdateView(BSModalUpdateView):
    model = Camera
    template_name = 'update_camera.html'
    form_class = CameraModelForm
    success_message = 'Success: Camera was updated.'
    success_url = reverse_lazy('index')


# Delete camera
class BookDeleteView(BSModalDeleteView):
    model = Camera
    template_name = 'delete_camera.html'
    success_message = 'Success: Camera was deleted.'
    success_url = reverse_lazy('index')