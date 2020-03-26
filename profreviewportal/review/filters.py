import django_filters
from .models import Review, Course, Prof
from . import models

from dal import autocomplete
from . import views


class ReviewFilter(django_filters.FilterSet):
    # code = django_filters.ModelChoiceFilter(
    #     queryset=Course.objects.all(),
    #     widget=autocomplete.ModelSelect2(url="review:code-autocomplete")
    # )
    # code = django_filters.ModelChoiceFilter(queryset=Course.objects.all(),
    #                                         widget=autocomplete.ModelSelect2(url='review:code-autocomplete'))

    #  prof=django_filters.CharFilter()

    class Meta:
        model = Review
        # widgets = {
        #     'code': autocomplete.ModelSelect2(url='review:code-autocomplete'),
        #     'prof': autocomplete.ModelSelect2(url='review:prof-autocomplete'),

        # }
        fields = ['code', 'prof']
