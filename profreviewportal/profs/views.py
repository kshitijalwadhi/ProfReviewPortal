from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse

# Create your views here.


def prof_homepage(request):
    return HttpResponse('Prof Homepage')
