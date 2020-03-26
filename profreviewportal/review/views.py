from django.shortcuts import render, redirect
from .models import Review, Prof, Course
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

from dal import autocomplete

from .filters import ReviewFilter

# Create your views here.


class CodeAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        qs = Course.objects.all()

        if self.q:
            qs = qs.filter(courseName__istartswith=self.q)

        return qs


class ProfAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        qs = Prof.objects.all()

        if self.q:
            qs = qs.filter(profname__istartswith=self.q)

        return qs


@login_required(login_url="/accounts/login")
def add_review(request):
    if request.method == 'POST':
        form = forms.AddReview(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            # return redirect('articles:list')
            return HttpResponse('added')
    else:
        form = forms.AddReview()
    return render(request, 'review/add_review.html', {'form': form})


def review_list(request):
    reviews = Review.objects.all().order_by('-date')
    return render(request, 'review/course_list.html', {'reviews': reviews})


def search(request):
    review_filter = ReviewFilter(request.GET, queryset=Review.objects.all())
    return render(request, 'review/search.html', {'filter': review_filter})
