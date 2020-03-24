from django.shortcuts import render, redirect
from .models import Review, Prof, Course
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.


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
