from . import models
from .mixins import AddClassNameMixin 

from django import forms
from django.core.exceptions import ValidationError

class RequestForm(AddClassNameMixin,forms.ModelForm):
    class_name = 'form-control'
    class Meta:
        model = models.Request
        exclude = ['viewed']
