from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    url(r'^$', views.courses_homepage, name="courses_homepage"),
]
