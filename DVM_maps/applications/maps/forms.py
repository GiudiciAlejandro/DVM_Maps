################################
# https://pypi.org/project/django-bootstrap-modal-forms/
# Revisar esto para tener un form como popup

from django import forms
from .models import Camera
from bootstrap_modal_forms.forms import BSModalModelForm

class CameraModelForm(BSModalModelForm):
   class Meta:
      model = Camera
      exclude = ('site',)


   

   