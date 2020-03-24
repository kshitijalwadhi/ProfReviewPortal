from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'review'

urlpatterns = [
    url('^add_review/$', views.add_review, name="create"),
]
