from django import forms
from . import models

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from dal import autocomplete
from .models import Block


class AddBlockField(forms.ModelForm):
    class Meta:
        model = models.Block
        fields = []
