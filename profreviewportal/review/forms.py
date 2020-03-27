from django import forms
from . import models

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from dal import autocomplete


class AddReview(forms.ModelForm):
    class Meta:
        model = models.Review
        widgets = {
            'code': autocomplete.ModelSelect2(url='review:code-autocomplete'),
            'prof': autocomplete.ModelSelect2(url='review:prof-autocomplete'),

        }
        fields = ['code', 'prof', 'comment',
                  'difficulty', 'contentquality', 'anonymous']


class AddCourse(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = ['courseName']


class AddProf(forms.ModelForm):
    class Meta:
        model = models.Prof
        fields = ['profname']
