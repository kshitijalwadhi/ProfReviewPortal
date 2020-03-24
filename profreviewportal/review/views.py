from django.shortcuts import render, redirect
from .models import Review, Prof, Course
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

from dal import autocomplete

# Create your views here.


# @login_required(login_url="/accounts/login")
class CodeAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        qs = Course.objects.all()

        if self.q:
            qs = qs.filter(courseName__istartswith=self.q)

        return qs


class ProfAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
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
