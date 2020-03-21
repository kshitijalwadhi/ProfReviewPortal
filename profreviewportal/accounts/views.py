from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse

# Create your views here.


def signup_view(request):
    return HttpResponse('Signup')


def login_view(request):
    return HttpResponse('Login')


def logout_view(request):
    return HttpResponse('Logout')
