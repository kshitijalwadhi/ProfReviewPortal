from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'profs'

urlpatterns = [
    url(r'^$', views.prof_homepage, name="prof_homepage"),
]
