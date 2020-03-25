from django import forms
from . import models

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
