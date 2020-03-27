from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from review.models import Course, Review, Prof, Warning
from django.contrib.auth.decorators import login_required
# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log the user in
            login(request, user)
            # return HttpResponse('Signed up')
            return redirect('review:search')  # see this redirect later
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                # return HttpResponse('Logged in')
                return redirect('review:search')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        # return HttpResponse('Logged out')
        return redirect('accounts:login')


@login_required(login_url="/accounts/login")
def profile_view(request):
    reviews = Review.objects.all().order_by('-date')
    warnings = Warning.objects.all().order_by('-date')
    return render(request, 'accounts/profile.html', {'reviews': reviews, 'warnings': warnings})
