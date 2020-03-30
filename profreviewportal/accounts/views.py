from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from review.models import Course, Review, Prof, Warning
from django.contrib.auth.decorators import login_required
from .forms import AddBlockField, AddLikeField
from .models import Block, LikesCount
from django.forms import ValidationError
from datetime import datetime, timedelta


# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        block_form = AddBlockField(request.POST)
        like_form = AddLikeField(request.POST)
        if form.is_valid():
            user = form.save()
            blockobj = block_form.save(commit=False)
            likeobj = like_form.save(commit=False)
            blockobj.user = user
            blockobj.block = False
            blockobj.save()
            likeobj.user = user
            likeobj.userlikes = 0
            likeobj.save()
            # log the user in
            login(request, user)
            # return HttpResponse('Signed up')
            return redirect('review:search')  # see this redirect later
    else:
        form = UserCreationForm()
        block_form = AddBlockField()
    return render(request, 'accounts/signup.html', {'form': form, 'block_form': block_form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user
            user = form.get_user()
            blocks = Block.objects.all()
            for block in blocks:
                if block.user == user and block.blockperm == True:
                    test = True
                    return render(request, 'accounts/blocked.html', {'test': test})
                elif block.user == user and block.tempban == True:
                    test = False
                    till = block.end
                    return render(request, 'accounts/blocked.html', {'test': test, 'till': till})
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
    ratings = LikesCount.objects.all()
    reviews = Review.objects.all().order_by('-date')
    warnings = Warning.objects.all().order_by('-date')
    return render(request, 'accounts/profile.html', {'reviews': reviews, 'warnings': warnings, 'ratings': ratings})
