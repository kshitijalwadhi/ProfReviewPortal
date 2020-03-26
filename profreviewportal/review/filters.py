import django_filters
from .models import Review, Course, Prof

from dal import autocomplete


class ReviewFilter(django_filters.FilterSet):
    # code = django_filters.ModelChoiceFilter(queryset=Review.objects.all(),
    # widget=autocomplete.ModelSelect2('review:code-autocomplete'))
    # code = django_filters.CharFilter(lookup_expr='icontains',
    #                                 widget=autocomplete.ModelSelect2(url='review:code-autocomplete'))
    #
    class Meta:
        model = Review
        widgets = {
            'code': autocomplete.ModelSelect2(url='review:code-autocomplete'),
            'prof': autocomplete.ModelSelect2(url='review:prof-autocomplete'),

        }
        fields = ['code', 'prof']
