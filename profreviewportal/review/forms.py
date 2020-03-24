from django import forms
from . import models


class AddReview(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ['code', 'prof', 'comment',
                  'difficulty', 'contentquality', 'author']
